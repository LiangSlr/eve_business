import sqlite3
import resell_profit_calculate


def get_type_data(type_id):
    """从sde中读取一个物品的数据"""
    sde = sqlite3.connect("E:\LHB/tools\eve\python/untitled1\eve.db")
    business_data = sqlite3.connect("E:\LHB/tools\eve\python/untitled1/business.db")
    cur = sde.cursor()  # sde游标
    cur.execute('select typeID, typeName, volume from invTypes where typeID between 34 and 40')
    cur_business = business_data.cursor()
    for i in range(1, 10000):
        # res = cur.fetchone()
        j = [i]
        cur_business.execute('insert into resell(typeID) values (?)', j)
    business_data.commit()
    cur_business.execute('select typeID, typeName, volume from resell')
    res_business = cur_business.fetchall()
    print(res_business)
    cur.close()
    cur_business.close()
    sde.close()
    business_data.close()
    return
    # return res


def update_one_row(type_id):
    """

    :return:
    """
    '''打开游标和数据库'''
    sde = sqlite3.connect("E:\LHB/tools\eve\python/untitled1\eve.db")
    business_data = sqlite3.connect("E:\LHB/tools\eve\python/untitled1/business.db")
    '''创建数据库游标，[]这个符号是因为需要更改type_id 格式'''
    cur = sde.cursor()
    cur_business = business_data.cursor()
    '''取出目标信息'''
    cur.execute('select typeID, typeName, volume from invTypes where typeID = ?', [type_id])
    res = cur.fetchall()
    '''将信息存入business''''''sql这句是真的low，编写效率极低，可以改进'''
    sql = "update resell set typeName = '" + res[0][1] + "', volume = " + str(res[0][2]) +" where typeID = " + str(res[0][0])
    cur_business.execute(sql)
    business_data.commit()
    # cur_business.execute('select typeID, typeName, volume from resell where typeID between 34 and 40')
    # res_business = cur_business.fetchall()
    # print(res_business)
    '''关闭游标和数据库'''
    cur.close()
    cur_business.close()
    sde.close()
    business_data.close()
    # print(type_id, '完成信息更新')


def update_resell_data_row(resell_data, type_id):
    """
    将物品倒卖利润更新至数据库
    :param resell_data: 物品信息，包含倒卖利润信息，resell——data是一个字典
    :return: 无
    """
    '''打开游标和数据库'''
    business_data = sqlite3.connect("E:\LHB/tools\eve\python\eve_business/business.db")
    cur_business = business_data.cursor()
    '''更新数据'''
    if resell_data:
        data = (
            resell_data['profit_jita_domain'], resell_data['margin_jita_domain'], resell_data['profit_ten_thousand_cube'], (type_id)
        )

        cur_business.executemany("update resell set "
                                 " profit = ?,"
                                 " profit_percent= ?,"
                                 " profit_ten_thousand_cube =?"
                                 " where typeID = ?", [data])
        business_data.commit()
        cur_business.close()
        business_data.close()
    else:
        cur_business.close()
        business_data.close()
        return
    # print(type_id , '完成更新')




