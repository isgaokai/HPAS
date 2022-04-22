# coding:utf-8
# @Project -> File     ：HPAS -> contentBot         
# @IDE      ：PyCharm
# @Author   ：Fenglchen
# @Date     ：2022/4/11 10:52
# @Software : macos python3.8
import json
import requests

# 转化为url字符串
def convent_url_str(url):
    # 转化哈希表
    convent_hashtable = {
        '/': '%252F',
        '?': '%253F',
        '=': '%253D',
        ':': '%253A',
        '&': '%26',

    }
    # 转化后的url
    result_url = ''
    # 进行转化
    for char in url:
        try:
            result_url += convent_hashtable[char]
        except KeyError:
            result_url += char
    # 返回结果
    return result_url

# 历史价格爬取bot
def history_price_bot(url):
    url = convent_url_str(url)
    history_url = 'https://apapia.manmanbuy.com/ChromeWidgetServices/WidgetServices.ashx'
    # session = requests.session()
    # 请求头
    headers = {
        'Host': 'apapia.manmanbuy.com',
        'Content-Type': 'application/x-www-form-urlencoded; charset=utf-8',
        'Proxy-Connection': 'close',
        'Cookie': 'ASP.NET_SessionId=uwhkmhd023ce0yx22jag2e0o;',
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_3 like Mac OS X) AppleWebKit/603.3.8 (KHTML, like Gecko) Mobile/14G60 mmbWebBrowse',
        'Content-Length': '457',
        'Accept-Encoding': 'gzip',
        'Connection': 'close',
    }
    # 携带参数
    post_data = 'c_devid=2C5039AF-99D0-4800-BC36-DEB3654D202C&username=&qs=true&c_engver=1.5.0&c_devtoken=&c_devmodel=iPhone%20SE&c_contype=wifi&' \
               't=1537348981671&c_win=w_320_h_568&p_url={}&' \
               'c_ostype=ios&jsoncallback=%3F&c_ctrl=w_search_trend0_f_content&methodName=getBiJiaInfo_wxsmall&c_devtype=phone&' \
               'jgzspic=no&c_operator=%E4%B8%AD%E5%9B%BD%E7%A7%BB%E5%8A%A8&c_appver=3.6.0&bj=false&c_dp=2&c_osver=10.3.3'.format(url)
    # session.headers.update(headers)
    request = requests.get(url=history_url,data=post_data,verify=False,headers=headers).text
    # {"ok": 0, "msg": "感谢您为我们找到失联的商品，我们正在抓紧收录，下次见面就有啦"}
    # 转为json
    item_js = json.loads(request)

    # 判断是否存在
    correct = item_js['ok']
    #0 <class 'int'>
    # 输入存在问题:
    if not correct:
        return None,None,None,None

    # 物品标题
    item_title = item_js['single']['title']
    # 商品最低价格
    item_lower_price = item_js['single']['lowerPrice']
    # 商品优惠后最低价格
    item_lower_price_yh = item_js['single']['lowerPriceyh']
    # 商品价格趋势
    item_price_trend = item_js['single']['jiagequshiyh']

    return  item_title,item_lower_price,item_lower_price_yh,item_price_trend

