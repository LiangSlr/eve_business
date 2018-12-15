import requests
import json
import numpy
import matplotlib.pyplot as mpl
import resell_profit_calculate as rps
import yaml
import sqlite3
import PyQt5
# import PyMySQL
# test = get_market_order(10000002, 34, 'sell')
# print(test)
'''
# plot, set grid and adjust axis num
# mpl.plot(price_average)
# mpl.grid(True)
# mpl.ylim(0, 10)
# mpl.xlim(0, len(price_average))
# mpl.show()
'''

'''test 函数'''


def test_sort():
    # list1 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    list1 = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    print(list1)
    sorted_list1 = quick_sort(list1, 0, len(list1))
    print(sorted_list1)


def test():
    pass
    # '''test sorted_order'''
    # market_order = get_market_order(10000043, 34, 'sell')
    # sorted_order = order_sort(market_order, 0, 60008494)
    # for order in sorted_order:
    #     print(order)
    # '''test profit_between_region'''
    # profit = profit_resell_one_type(10000002, 10000043, 34)
    # profit = profit_resell_one_type(10000002, 10000043, 35)
def get_sde():
    '''获取in_type内容，最好是能存成一个文件，避免经常使用request'''
    contid = 0# 已获得的条目数
    results = []# 存储获取内容
    '''获取第一次内容'''
    request_link_base = 'https://evekit-sde.orbital.enterprises/20181009/api/ws/v20181009/inv/type?contid='
    request_link = request_link_base + str(contid)
    next = requests.get(request_link).json()
    results = next
    '''循环直至获取到的内容为空，即contid为0'''
    # while len(next) > 0 & contid < 100:
    #     results.extend(next)
    #     contid += len(next)
    #     request_link = request_link_base + str(contid)
    #     next = requests.get(request_link).json()
    return results


def test_sql():
    """py SQlite 使用方法"""
    '''连接数据库
    #   数据库操作方法     cursor()    commit()         roolback()       close()
                        创建游标       事物提交（确认）     事物回滚（撤销）    关闭数据库连接
    '''
    con = sqlite3.connect("E:\LHB/tools\eve\python/untitled1\eve.db")
    '''创建游标，游标，是数据库查询的工具
        # 游标有很多使用方法： 执行sql语句 执行多条sql语句 close关闭游标  创建游标
                            execute()   executemany     close       con.cursor()
        从结果中取一条记录   从结果中取多条记录   取全部记录   游标滚动    
            fetchone()      fetchmany()      fetchall()  scroll()
    '''
    cur = con.cursor()
    '''查询数据
        查询 select ..... from 表  
        插入 insert into 表（列， 列） values（值，值）
        更新 update 表 set 列 = 值
        条件语句 where， between， in， like， group by， order by
    '''
    cur.execute('SELECT typeID, typeName, volume FROM invTypes')
    res = cur.fetchmany(35)
    print(res)
    '''关闭数据库，关闭游标
    '''
    cur.close()
    con.close()
    '''
        数据库的创建直接连接数据库，如果没有自动创建
        列表的创建使用 create table xxx（列名 数据类型，列名 数据类型）
        数据类型有 int（size） 整数，      decimal（size，d）， 
        小数 char（size） 固定长度字符串，  varchar（size） 变长度字符串， data(yyyymmdd) 日期
        其中 size均为数字位数，字符长度的意思，d表示小数点右侧最大位数
    '''

'''函数运行'''
# init_set()
# sde = get_sde()
# print(sde[30:31])
# test_sql()
