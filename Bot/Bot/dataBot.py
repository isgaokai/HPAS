# coding:utf-8
# @Project -> File     ：HPAS -> dataBot         
# @IDE      ：PyCharm
# @Author   ：Fenglchen
# @Date     ：2022/4/12 14:35
# @Software : macos python3.8

# 时间处理
def date_treat_bot(date):
    """
    :param date: Tuple example:(2022, 1, 1)
    :return: String example:2022-1-1
    """
    # 判断输入是否有效
    if not date or len(date) != 3:
        return False

    # 获取年月日
    year = date[0]
    month = date[1]
    day = date[2]

    # 对获取的数据进行处理
    if month  == 12:
        year += 1
        month = 1
    else:
        month += 1

    # 返回结果
    return '{}-{}-{}'.format(year,month, day)

# 数据处理
def data_treat_bot(item_price_trend):
    """
    :param item_price_trend: List of historical prices for good
    :return:
    """
    # 判断是否有效
    if not item_price_trend:
        return False

    # 返回数据
    date_ = []
    price_ = []
    tip_ = []

    # 将初始数据进行处理
    item_price_trend = eval(item_price_trend.replace('Date.UTC',''))

    # 对初步处理后的数据进行切分
    for data in item_price_trend:
        date_.append(date_treat_bot(data[0]))
        price_.append(data[1])
        tip_.append(data[2])

    # 返回结果
    return date_,price_,tip_
