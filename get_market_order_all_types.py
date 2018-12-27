import requests
import json
import sqlite3
import time
import queue
import threading


def get_market_orders(region_id, q, order_type='all', page=1, *type_id):
    '''获取市场订单，当未输入物品类型type_id时，将下载所有市场订单（根据page有所不同），当输入物品类型时，将下载该物品的订单
        待优化：一个物品的订单有可能超过1000个，也就是超过1页，如果存在这种可能性就需要优化后一种功能
        region为星域id
        q为多线程操作时需要使用的队列
        order_type为订单类型，分别是sell, buy, all
    '''
    try:
        if len(type_id) == 0:  # 如果物品类型为空，即没有输入物品类型，则返回所有物品类型的订单数据
            request_link = 'https://esi.evetech.net/latest/markets/' \
                           + str(region_id) + '/orders/?datasource=tranquility&order_type=all&page=' \
                           + str(page)
        else:  # 如果物品类型不为空，则返回该物品的订单数据
            request_link = 'https://esi.evetech.net/latest/markets/' \
                           + str(region_id) + '/orders/?datasource=tranquility&order_type=' \
                           + order_type + '&page=1&type_id=' \
                           + str(type_id[0])
        market_orders = requests.get(request_link).json()  # 获得市场订单，并更改数据类型为list
        q.put(market_orders)  # 将订单数据放入队列
    except:
        print('订单爬取出错')


def save_market_orders(region_id):
    """
    获取所有订单数据，并存储至数据库，business_data, market_order
    :return: none
    """
    q = queue.Queue()
    if region_id == 10000002:  # 不同星域订单数量不同
        total_page = 310
    else:
        total_page =200
    print("正在爬取%d个订单数据，region_id:"%(total_page), region_id)
    for page in range(1, total_page):  # 读取订单的多线程
        thread_get = threading.Thread(target=get_market_orders, args=(region_id, q, 'all', page))
        thread_get.start()
    thread_insert = threading.Thread(target=market_order_combine, args=(region_id, q))  # 存储订单的线程
    thread_insert.start()
    thread_insert.join()  # 阻塞主线程，避免多个线程同时操作数据库


def insert_orders_into_database(region_id, market_orders):
    """
    将订单数据批量加入到数据库中
    :param market_orders:list，包含至多1000个订单的信息
    :param region_id 星域id
    :return:none
    """
    business_data = sqlite3.connect("E:\LHB/tools\eve\python/eve_business/business.db")
    cur_business = business_data.cursor()
    data = []
    for order in market_orders:
        data.append((order['is_buy_order'], order['location_id'], order['order_id'],
                order['price'], order['system_id'], order['type_id'], region_id))  # 将数据整理为tuple格式
    cur_business.execute("drop index index_market_orders_typeid")
    business_data.commit()
    cur_business.executemany("insert into market_orders (is_buy_order, location_id, order_id, price, system_id, type_id, region_id) "
                             "values (?, ?, ?, ?, ?, ?, ?)", data)
    business_data.commit()
    if region_id == 10000002:  # 删除不需要的订单数据
        cur_business.execute("delete from market_orders where region_id = 10000002 and location_id != 60003760")
    else:
        cur_business.execute("delete from market_orders where region_id = 10000043 and location_id != 60008494")
    cur_business.execute("create index index_market_orders_typeid on market_orders(type_id)")
    business_data.commit()
    print('orders in %d have been inserted\n'%(region_id))
    '''关闭数据库'''
    cur_business.close()
    business_data.close()


def market_order_combine(region_id, q):
    """
    将所有订单连接为一个长的list，后续insert速度快一些
    :param region_id: 星域id
    :param q: 订单队列
    :return: None
    """
    market_orders = q.get()
    while True:
        try:
            market_orders += q.get(block=True, timeout=5)   # 从队列中获取数据, 等待延时5秒
        except:
            print('订单数据爬取完成，正在存储订单数据')
            # traceback.print_exc()
            break
    insert_orders_into_database(region_id, market_orders)


def delete_data_in_market_orders(region_id):
    """
    删除数据库中的数据
    :param region_id: 星域id
    :return:
    """
    '''打开数据库'''
    connection = sqlite3.connect("E:\LHB/tools\eve\python/eve_business/business.db")
    cur = connection.cursor()
    '''删除数据'''
    cur_execute = "delete from market_orders where region_id = " + str(region_id)
    cur.execute(cur_execute)
    connection.commit()
    print("旧数据已经删除")
    '''关闭数据库'''
    cur.close()
    connection.close()


if __name__ == '__main__':
    start = time.time()
    region_ids = [10000002, 10000043]
    delete_data_in_market_orders(region_ids[0])
    delete_data_in_market_orders(region_ids[1])
    save1 = threading.Thread(save_market_orders(region_ids[0]))
    save1.start()
    save2 = threading.Thread(save_market_orders(region_ids[1]))
    save2.start()
    print(time.time() - start)



