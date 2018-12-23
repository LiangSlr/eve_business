import sqlite3
import time
import resell_profit_calculate
import numpy as np

def get_type_data(type_id):
    """从sde中读取一个物品的数据"""
    sde = sqlite3.connect("E:\LHB/tools\eve\python\eve_business\eve.db")
    business_data = sqlite3.connect("E:\LHB/tools\eve\python\eve_business/business.db")
    cur = sde.cursor()  # sde游标
    cur.execute('select typeID, typeName, volume from invTypes where typeID between 34 and 40')
    cur_business = business_data.cursor()
    for i in range(100000, 400000):
        # res = cur.fetchone()
        j = [i]
        cur_business.execute('insert into resell(typeID) values (?)', j)
    business_data.commit()
    cur_business.execute('select typeID, typeName, volume from resell')
    res_business = cur_business.fetchall()
    # print(res_business)
    cur.close()
    cur_business.close()
    sde.close()
    business_data.close()
    return
    # return res


def update_infor_resell(type_id):
    """
    每次下载了新的SDE都需要对自己建立的数据库做出匹配，更新resell数据库物品信息
    :type_id 物品信息
    :return:none
    """
    '''打开游标和数据库'''
    sde = sqlite3.connect("E:\LHB/tools\eve\python\eve_business\eve.db")
    business_data = sqlite3.connect("E:\LHB/tools\eve\python\eve_business/business.db")
    '''创建数据库游标'''
    cur_business = business_data.cursor()
    cur = sde.cursor()
    '''取出目标信息'''
    cur.execute('select typeID, typeName, volume from invTypes')
    res = cur.fetchall()
    for re in res:
        '''将信息存入business''''''sql这句是真的low，编写效率极低，可以改进;还可以继续改进为executemany'''
        cur_business.execute("update resell set typeName =?, volume =? where typeID = ?",
                                 (str(re[1]), str(re[2]), str(re[0])))
        print('typeid', re[0], '已修改，等待提交')
        re = cur.fetchone()
    # else:
    #     # print("invType 数据库中无此物品，typeid", type_id)
    #     print('更新完成')
    #     pass
    print('所有更新已提交')
    business_data.commit()
    '''关闭游标和数据库'''
    cur_business.close()
    business_data.close()
    cur.close()
    sde.close()



    # print(type_id, '完成信息更新')


def update_resell_data_row(goods):
    """
    将物品倒卖利润更新至数据库
    :param resell_data: 物品信息，包含倒卖利润信息，resell_data是一个字典
    :return: 无
    """
    '''打开游标和数据库'''
    business_data = sqlite3.connect("E:\LHB/tools\eve\python\eve_business/business.db")
    cur_business = business_data.cursor()
    '''更新数据'''
    data = []
    i = 0;
    print("正在更新数据")
    start = time.time()
    for key in goods:
        data.append(
                    (goods[key]['profit_jita_domain'],  goods[key]['margin_jita_domain'],
                    goods[key]['profit_ten_thousand_cube'], key) )
        i += 1
    cur_business.executemany("update resell set "
                             " profit = ?,"
                             " profit_percent= ?,"
                             " profit_ten_thousand_cube =?"
                             " where typeID = ?", data)
    business_data.commit()
    print('数据更新完毕,耗时：', time.time() - start)
    cur_business.close()
    business_data.close()
    # else:
    #     cur_business.close()
    #     business_data.close()
    #     return
    # print(type_id , '完成更新')


def update_resell_infor():
    """
    该函数的目的为此
    :return: None

    """



if __name__ == '__main__':
    # get_type_data(1)
    # type_ids = tuple(range(10000, 400000))
    # update_infor_resell(type_ids)

    business_data = sqlite3.connect("E:\LHB/tools\eve\python\eve_business/business.db")
    '''创建数据库游标'''
    cur_business = business_data.cursor()
    cur_business.execute("select typeID from resell")
    re = cur_business.fetchone()
    cur_business.execute("delete from resell where typeID > 50000 ")
    # while re:
    #     if re > 50000 :
    #         pass
    #     else:
    #         cur_business.execute("delete from resell where typeID = ? ", (str(re[0])))
    business_data.commit()
    cur_business.close()
    business_data.close()