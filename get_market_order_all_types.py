import requests
import json
import sqlite3
import time


def get_market_orders(region_id, order_type='all', page='1', *type_id):
    '''获取市场订单，当为输入物品类型type_id时，将下载所有市场订单（根据page有所不同），当输入物品类型时，将下载该物品的订单
        待优化：一个物品的订单有可能超过1000个，也就是超过1页，如果存在这种可能性就需要优化后一种功能
        region为星域id
        order_type为订单类型，分别是sell buy all
    '''
    region_id = str(region_id)
    order_type = str(order_type)
    if len(type_id) == 0:  # 如果物品类型为空，即没有输入物品类型，则返回所有物品类型的订单数据
        request_link = 'https://esi.evetech.net/latest/markets/'\
                       + region_id + '/orders/?datasource=tranquility&order_type=all&page=' \
                       + page
    else:  # 如果物品类型不为空，则返回该物品的订单数据
        request_link = 'https://esi.evetech.net/latest/markets/' \
                       + region_id + '/orders/?datasource=tranquility&order_type=' \
                       + order_type + '&page=1&type_id=' \
                       + str(type_id[0])
    print('prepare download orders')
    market_order = requests.get(request_link).json()  # 获得市场订单，并更改数据类型为list
    print('market orders in page', page, 'have been downloaded')
    return market_order


def save_market_orders(region_id):
    """
    获取所有订单数据，并存储至数据库，business_data, market_order
    :return: none
    """
    order_temp = get_market_orders(region_id)
    page = 1
    while len(order_temp) != 0:
        page += 1
        insert_orders_in_database(region_id, order_temp)
        order_temp = get_market_orders(region_id, 'all', str(page))

    """ 用来将数据存储在json文件中的代码，但文件太大了，不便于操作
    '''清空文件'''
    file_path = 'E:\LHB\\tools\eve\python\\untitled1\market_order.json'
    with open(file_path, "w") as fp:
        fp.truncate()
    """


def insert_orders_in_database(region_id, market_orders):
    """
    将一页的订单数据逐行加入到数据库中
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
    cur_business.executemany("insert into market_orders (is_buy_order, location_id, order_id, price, system_id, type_id, region_id) "
                             "values (?, ?, ?, ?, ?, ?, ?)", data)
    business_data.commit()
    print('orders have been inserted\n')
    '''关闭数据库'''
    cur_business.close()
    business_data.close()


def store_all_market_orders():
    market_order = [{"duration": 90, "is_buy_order": False, "issued": "2018-11-07T03:55:30Z", "location_id": 60001801,
                    "min_volume": 1, "order_id": 5233442817, "price": 8000.0, "range": "region", "system_id": 30000162,
                    "type_id": 251, "volume_remain": 4994, "volume_total": 5000},
                    {"duration": 90, "is_buy_order": False, "issued": "2018-11-07T03:55:30Z", "location_id": 60001801,
                    "min_volume": 1, "order_id": 5233442817, "price": 8000.0, "range": "region", "system_id": 30000162,
                    "type_id": 251, "volume_remain": 4994, "volume_total": 5000}]
    insert_orders_in_database(market_order)


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
    '''关闭数据库'''
    cur.close()
    connection.close()


if __name__ == '__main__':
    region_ids = [10000002, 10000043]
    # delete_data_in_market_orders(region_ids[0])
    # save_market_orders(region_ids[0])
    delete_data_in_market_orders(region_ids[1])
    save_market_orders(region_ids[1])




