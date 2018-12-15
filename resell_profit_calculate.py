import requests
import json
import numpy
import matplotlib.pyplot as mpl
import tkinter as tk
from sql_data_handle import *
"""已完成，进一步任务，对订单排序，然后找出最低售价，再找出售地点的最低售价，然后计算利润"""
"""已完成，完成之后尝试开展对多个物品，甚至所有物品计算倒卖利润,
    问题：由于目前的方式是多次请求get，由于网速的原因导致进程较慢，
    因此后续改进为一次性在第一次调用get类函数时获得所有物品order，history，并将这些数据分类存进一个global字典中，规避网络问题"""
"""之后引入数据库，计算万方利润率，和满载强暴系数"""
"""万方利润"""


goods = {}


def init_set(type_ids):
    """初始化"""
    '''数据初始化'''
    global goods
    goods = {34: {'name': 'tritanium', 'volume': 0.01, 'profit': 0.1, 'margin': 1, 'profit_ten_thousand_cube':1},
             35:{}
             }
    for i in range(36, type_ids):
        goods[i] = {}


def quick_sort(list, start, end):
    """快速排序法排序列表
        list：需要排序的列表
        start：排序开始处，第一次调用时一般为0
        end：排序结束处，第一次调用时一般为list的长度减1
    """
    if start >= end:
        return
    index = start
    for i in range(start+1, end):
        # if list[i] < list[index]:
        if list[i]['price'] < list[index]['price']:
            tmp = list[i]
            del list[i]
            list.insert(index, tmp)
            index += 1
    quick_sort(list, start=start, end=index)
    quick_sort(list, start=index+1, end=len(list))
    return list


def get_market_order(region_id, type_id, order_type):
    """获取市场订单
        region为星域id
        type_id为物品id
        order_type为订单类型，分别是sell buy all
    """
    region_id = str(region_id)
    type_id = str(type_id)  # 将输入转为字符串，增加鲁棒性
    order_type = str(order_type)
    request_link = 'https://esi.evetech.net/latest/markets/' + region_id + '/orders/?datasource=tranquility&order_type='+ order_type + '&page=1&type_id=' + type_id
    market_order = requests.get(request_link).json()  # 获得市场订单,requests返回的数据类型是一种特定的类型不可以直接操作，需要用.json进行更改，这里改为了list类型
    return market_order


def get_market_history(region_id, type_id):
    '''获取市场历史数据
        region为星域id
        type_id为物品id
    '''
    region_id = str(region_id)
    type_id = str(type_id)# 将输入转为字符串，增加鲁棒性
    request_link = 'https://esi.evetech.net/latest/markets/' + region_id + '/history/?datasource=tranquility&type_id=' + type_id
    market_history = requests.get(request_link)
    market_history = market_history.json()
    '''    
    print(r.json())
    print(r_json[0]['average'])
    '''
    return market_history


def order_sort(market_orders, sequence_type, location_id):
    """
    根据需求将订单排序
    market_orders 市场订单
    sequence_type 排序方式 0 从小到大
    location_id 目标空间站
    :return:
    """
    '''只保留目标空间站的订单'''
    orders_in_location = []
    for order in market_orders:
        if order['location_id'] == location_id:
            orders_in_location.append(order)
        else:
            pass
    '''按照sequence_type指定的排序方式排序'''
    orders_sorted = quick_sort(orders_in_location, 0, end=len(orders_in_location))

    return orders_sorted


def profit_resell_one_type(type_id, route=1):
    """
    计算两个星域之间某个商品的利润率
        type_id为物品id
        route 1从吉他到多美，0从多美到吉他
    :return:
    """
    global goods
    min_price = {}
    con = sqlite3.connect("E:\LHB/tools\eve\python/eve_business/business.db")
    cur = con.cursor()

    price = cur.execute('select price from market_orders '
                        'where type_id = ' + str(type_id) + ' and region_id = 10000002 and is_buy_order = 0 ' \
                        'order by price')  # 按照从低到高的顺序取价格, 吉他物品
    # print(cur.fetchone(), type(cur.fetchone()))
    if cur.fetchone() != None:
        min_price['jita'] = cur.fetchone()[0]  # 最低价格
    else:
        print("吉他没有物品", type_id, "号物品的订单")
        return
    price = cur.execute("select price from market_orders "
                         "where type_id = " + str(type_id) + " and region_id = 10000043 and is_buy_order = 0 "
                         "order by price")  # 按照从低到高的顺序取价格, 多美物品
    if cur.fetchone() != None:
        min_price['domain'] = cur.fetchone()[0]  # 最低价格
    else:
        return

    cur.close()
    con.close()

    '''利润和利润率计算'''
    if route:
        profit = min_price['domain'] - min_price['jita']
        margin = profit / min_price['jita']  # 毛利润率,未考虑税
        # profit_margin  # 净利润
    else:
        profit = min_price['jita'] - min_price['domain']
        margin = profit / min_price['domain']  # 毛利润率,未考虑税

    goods[type_id]['profit_jita_domain'] = round(profit, 3)
    goods[type_id]['margin_jita_domain'] = round(margin * 100, 3)  # 计算利润和利润率，用round取三位小数
    type_volume = 0.01
    profit_ten_thousand_cube(profit, type_volume, type_id)


def profit_ten_thousand_cube(profit, type_volume, type_id):
    """计算异地万方利润"""
    '''
        profit 物品单件利润
        volume 物品单件体积
        profit_ten_thousand_cube 一万方体积的该物品，利润为多少
    '''
    number_ten_thousand_cube = 10000 / type_volume
    goods[type_id]['profit_ten_thousand_cube'] = round(profit * number_ten_thousand_cube, 3)


def resell(type_ids):
    for i in range(34, type_ids):
        profit_resell_one_type(i)
        '''更新内容至business_data'''
        update_resell_data_row(goods[i], i)
        print('倒卖利润数据更新完成')


if __name__ == '__main__':
    '''计算吉他到艾玛，一个物品的利润和利润率'''
    init_set(500)
    resell(500)
    # profit_resell_one_type(34, 0)
    # print(goods[34])


