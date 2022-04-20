# coding:utf-8
import json
import requests
from django.shortcuts import render

# Create your views here.

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
    print(result_url)
    # 返回结果
    return result_url

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
    print(request)
    # 转为json
    item_js = json.loads(request)
    # 物品标题
    item_title = item_js['single']['title']
    # 商品最低价格
    item_lower_price = item_js['single']['lowerPrice']
    # 商品优惠后最低价格
    item_lower_price_yh = item_js['single']['lowerPriceyh']
    # 商品价格趋势
    item_price_trend = item_js['single']['jiagequshiyh']

# history_price_bot('https://item.jd.com/100011203359.html')
jiagequshi  = "[Date.UTC(2021,3,21),5999.00,\"购买1件,当前价:6799.00,优惠券：满5000减800\"],[Date.UTC(2021,3,22),5999.00,\"购买1件,当前价:6799.00,优惠券：满5000减800\"],[Date.UTC(2021,3,23),5999.00,\"5999元\"],[Date.UTC(2021,3,24),6799.0,\"\"],[Date.UTC(2021,3,25),5999.00,\"购买1件,当前价:6799.00,优惠券：满5000减800\"],[Date.UTC(2021,3,26),5999.00,\"购买1件,当前价:6799.00,优惠券：满5000减800\"],[Date.UTC(2021,3,27),5899.00,\"购买1件,当前价:6799.00,优惠券：满5000减900\"],[Date.UTC(2021,3,28),5899.00,\"购买1件,当前价:6799.00,优惠券：满5000减900\"],[Date.UTC(2021,3,29),5999.00,\"购买1件,当前价:6799.00,优惠券：满5000减800\"],[Date.UTC(2021,3,30),5999.00,\"购买1件,当前价:6799.00,优惠券：满5000减800\"],[Date.UTC(2021,4,1),5999.00,\"购买1件,当前价:6799.00,优惠券：满5000减800\"],[Date.UTC(2021,4,2),5999.00,\"购买1件,当前价:6799.00,优惠券：满5000减800\"],[Date.UTC(2021,4,3),5999.00,\"购买1件,当前价:6799.00,优惠券：满5000减800\"],[Date.UTC(2021,4,4),5999.00,\"购买1件,当前价:6799.00,优惠券：满5000减800\"],[Date.UTC(2021,4,5),5999.00,\"购买1件,当前价:6799.00,优惠券：满5000减800\"],[Date.UTC(2021,4,6),5999.00,\"5999元包邮（需用券）\"],[Date.UTC(2021,4,7),5999.00,\"购买1件,当前价:6799.00,优惠券：满5000减800\"],[Date.UTC(2021,4,8),5999.00,\"购买1件,当前价:6799.00,优惠券：满5000减800\"],[Date.UTC(2021,4,9),5999.00,\"购买1件,当前价:6799.00,优惠券：满5000减800\"],[Date.UTC(2021,4,10),5999.00,\"购买1件,当前价:6799.00,优惠券：满5000减800\"],[Date.UTC(2021,4,11),5999.00,\"购买1件,当前价:6799.00,优惠券：满5000减800\"],[Date.UTC(2021,4,12),5999.00,\"购买1件,当前价:6799.00,优惠券：满5000减800\"],[Date.UTC(2021,4,13),5999.00,\"购买1件,当前价:6799.00,优惠券：满5000减800\"],[Date.UTC(2021,4,14),5999.00,\"购买1件,当前价:6799.00,优惠券：满5000减800\"],[Date.UTC(2021,4,15),5999.00,\"购买1件,当前价:6799.00,优惠券：满5000减800\"],[Date.UTC(2021,4,16),5999.00,\"购买1件,当前价:6799.00,优惠券：满5000减800\"],[Date.UTC(2021,4,17),5999.00,\"购买1件,当前价:6799.00,优惠券：满5000减800\"],[Date.UTC(2021,4,18),5999.00,\"购买1件,当前价:6799.00,优惠券：满5000减800\"],[Date.UTC(2021,4,19),5999.00,\"购买1件,当前价:6799.00,优惠券：满5000减800\"],[Date.UTC(2021,4,20),5999.00,\"购买1件,当前价:6799.00,优惠券：满5000减800\"],[Date.UTC(2021,4,21),5999.00,\"购买1件,当前价:6799.00,优惠券：满5000减800\"],[Date.UTC(2021,4,22),5999.00,\"购买1件,当前价:6799.00,优惠券：满5000减800\"],[Date.UTC(2021,4,23),5999.00,\"购买1件,当前价:6799.00,优惠券：满5000减800\"],[Date.UTC(2021,4,24),5899.00,\"购买1件,当前价:6799.00,优惠券：满5000减900\"],[Date.UTC(2021,4,25),5999.00,\"购买1件,当前价:6799.00,优惠券：满5000减800\"],[Date.UTC(2021,4,26),5899.00,\"购买1件,当前价:6799.00,优惠券：满5000减900\"],[Date.UTC(2021,4,27),5899.00,\"购买1件,当前价:6799.00,优惠券：满5000减900\"],[Date.UTC(2021,4,28),5899.00,\"购买1件,当前价:6799.00,优惠券：满5000减900\"],[Date.UTC(2021,4,29),5808.00,\"购买1件,当前价:6708.00,优惠券：满5000减900\"],[Date.UTC(2021,4,30),5808.00,\"购买1件,当前价:6708.00,优惠券：满5000减900\"],[Date.UTC(2021,4,30),5708.00,\"购买1件,当前价:6708.00,优惠券：满4000减1000\"],[Date.UTC(2021,5,1),5708.00,\"购买1件,当前价:6708.00,优惠券：满4000减1000\"],[Date.UTC(2021,5,2),5308.00,\"5308元包邮（需用券）\"],[Date.UTC(2021,5,3),5708.00,\"购买1件,当前价:6708.00,优惠券：满4000减1000\"],[Date.UTC(2021,5,4),5999.00,\"购买1件,当前价:6799.00,优惠券：满4000减800\"],[Date.UTC(2021,5,5),5999.00,\"购买1件,当前价:6799.00,优惠券：满4000减800\"],[Date.UTC(2021,5,6),5999.00,\"购买1件,当前价:6799.00,优惠券：满4000减800\"],[Date.UTC(2021,5,7),5999.00,\"购买1件,当前价:6799.00,优惠券：满4000减800\"],[Date.UTC(2021,5,8),5999.00,\"购买1件,当前价:6799.00,优惠券：满4000减800\"],[Date.UTC(2021,5,9),5999.00,\"购买1件,当前价:6799.00,优惠券：满4000减800\"],[Date.UTC(2021,5,10),5999.00,\"购买1件,当前价:6799.00,优惠券：满4000减800\"],[Date.UTC(2021,5,11),5999.00,\"购买1件,当前价:6799.00,优惠券：满4000减800\"],[Date.UTC(2021,5,12),5999.00,\"购买1件,当前价:6799.00,优惠券：满4000减800\"],[Date.UTC(2021,5,13),5999.00,\"购买1件,当前价:6799.00,优惠券：满4000减800\"],[Date.UTC(2021,5,14),5999.00,\"购买1件,当前价:6799.00,优惠券：满4000减800\"],[Date.UTC(2021,5,15),5309.00,\"5309元包邮（需用券）\"],[Date.UTC(2021,5,16),6199.00,\"购买1件,当前价:6799.00,优惠券：满4000减600\"],[Date.UTC(2021,5,17),6199.00,\"购买1件,当前价:6799.00,优惠券：满4000减600\"],[Date.UTC(2021,5,18),6109.00,\"购买1件,当前价:6709.00,优惠券：满4000减600\"],[Date.UTC(2021,5,19),6109.00,\"购买1件,当前价:6709.00,优惠券：满4000减600\"],[Date.UTC(2021,5,20),6199.00,\"购买1件,当前价:6799.00,优惠券：满4000减600\"],[Date.UTC(2021,5,21),6199.00,\"购买1件,当前价:6799.00,优惠券：满4000减600\"],[Date.UTC(2021,5,22),6199.00,\"购买1件,当前价:6799.00,优惠券：满4000减600\"],[Date.UTC(2021,5,23),6199.00,\"购买1件,当前价:6799.00,优惠券：满4000减600\"],[Date.UTC(2021,5,24),6199.00,\"购买1件,当前价:6799.00,优惠券：满4000减600\"],[Date.UTC(2021,5,25),6199.00,\"购买1件,当前价:6799.00,优惠券：满4000减600\"],[Date.UTC(2021,5,26),6199.00,\"购买1件,当前价:6799.00,优惠券：满4000减600\"],[Date.UTC(2021,5,27),6199.00,\"购买1件,当前价:6799.00,优惠券：满4000减600\"],[Date.UTC(2021,5,28),6199.00,\"购买1件,当前价:6799.00,优惠券：满4000减600\"],[Date.UTC(2021,5,29),6199.00,\"购买1件,当前价:6799.00,优惠券：满4000减600\"],[Date.UTC(2021,5,30),6199.00,\"购买1件,当前价:6799.00,优惠券：满4000减600\"],[Date.UTC(2021,6,1),5999.00,\"购买1件,当前价:6599.00,优惠券：满4000减600\"],[Date.UTC(2021,6,2),5999.00,\"购买1件,当前价:6599.00,优惠券：满4000减600\"],[Date.UTC(2021,6,3),5999.00,\"购买1件,当前价:6599.00,优惠券：满4000减600\"],[Date.UTC(2021,6,4),5999.00,\"购买1件,当前价:6599.00,优惠券：满4000减600\"],[Date.UTC(2021,6,5),5999.00,\"购买1件,当前价:6599.00,优惠券：满4000减600\"],[Date.UTC(2021,6,6),5999.00,\"购买1件,当前价:6599.00,优惠券：满4000减600\"],[Date.UTC(2021,6,7),5999.00,\"购买1件,当前价:6599.00,优惠券：满4000减600\"],[Date.UTC(2021,6,8),5999.00,\"购买1件,当前价:6599.00,优惠券：满4000减600\"],[Date.UTC(2021,6,9),5999.00,\"购买1件,当前价:6599.00,优惠券：满4000减600\"],[Date.UTC(2021,6,10),5999.00,\"购买1件,当前价:6599.00,优惠券：满4000减600\"],[Date.UTC(2021,6,11),5999.00,\"购买1件,当前价:6599.00,优惠券：满4000减600\"],[Date.UTC(2021,6,12),5999.00,\"购买1件,当前价:6599.00,优惠券：满4000减600\"],[Date.UTC(2021,6,13),5999.00,\"购买1件,当前价:6599.00,优惠券：满4000减600\"],[Date.UTC(2021,6,14),5999.00,\"购买1件,当前价:6599.00,优惠券：满4000减600\"],[Date.UTC(2021,6,15),5799.00,\"购买1件,当前价:6599.00,优惠券：满4000减800\"],[Date.UTC(2021,6,16),5799.00,\"购买1件,当前价:6599.00,优惠券：满4000减800\"],[Date.UTC(2021,6,17),5799.00,\"购买1件,当前价:6599.00,优惠券：满4000减800\"],[Date.UTC(2021,6,18),5799.00,\"购买1件,当前价:6599.00,优惠券：满4000减800\"],[Date.UTC(2021,6,19),5799.00,\"购买1件,当前价:6599.00,优惠券：满4000减800\"],[Date.UTC(2021,6,20),5799.00,\"购买1件,当前价:6599.00,优惠券：满4000减800\"],[Date.UTC(2021,6,21),5799.00,\"购买1件,当前价:6599.00,优惠券：满4000减800\"],[Date.UTC(2021,6,22),5699.00,\"购买1件,当前价:6599.00,优惠券：满4000减900\"],[Date.UTC(2021,6,23),5699.00,\"购买1件,当前价:6599.00,优惠券：满4000减900\"],[Date.UTC(2021,6,24),5699.00,\"购买1件,当前价:6599.00,优惠券：满4000减900\"],[Date.UTC(2021,6,25),5699.00,\"购买1件,当前价:6599.00,优惠券：满4000减900\"],[Date.UTC(2021,6,26),5699.00,\"购买1件,当前价:6599.00,优惠券：满4000减900\"],[Date.UTC(2021,6,27),5699.00,\"购买1件,当前价:6599.00,优惠券：满4000减900\"],[Date.UTC(2021,6,28),5699.00,\"购买1件,当前价:6599.00,优惠券：满4000减900\"],[Date.UTC(2021,6,29),5699.00,\"购买1件,当前价:6599.00,优惠券：满4000减900\"],[Date.UTC(2021,6,30),5699.00,\"购买1件,当前价:6599.00,优惠券：满4000减900\"],[Date.UTC(2021,6,30),5699.00,\"购买1件,当前价:6599.00,优惠券：满4000减900\"],[Date.UTC(2021,7,1),5999.00,\"购买1件,当前价:6599.00,优惠券：满4000减600\"],[Date.UTC(2021,7,2),5999.00,\"购买1件,当前价:6599.00,优惠券：满4000减600\"],[Date.UTC(2021,7,3),5699.00,\"购买1件,当前价:6599.00,优惠券：满4000减900\"],[Date.UTC(2021,7,4),5699.00,\"购买1件,当前价:6599.00,优惠券：满4000减900\"],[Date.UTC(2021,7,5),5699.00,\"购买1件,当前价:6599.00,优惠券：满4000减900\"],[Date.UTC(2021,7,6),5699.00,\"购买1件,当前价:6599.00,优惠券：满4000减900\"],[Date.UTC(2021,7,7),5699.00,\"购买1件,当前价:6599.00,优惠券：满4000减900\"],[Date.UTC(2021,7,8),5699.00,\"购买1件,当前价:6599.00,优惠券：满4000减900\"],[Date.UTC(2021,7,9),5699.00,\"购买1件,当前价:6599.00,优惠券：满4000减900\"],[Date.UTC(2021,7,10),5699.00,\"购买1件,当前价:6599.00,优惠券：满4000减900\"],[Date.UTC(2021,7,11),5699.00,\"购买1件,当前价:6599.00,优惠券：满4000减900\"],[Date.UTC(2021,7,12),5699.00,\"购买1件,当前价:6599.00,优惠券：满4000减900\"],[Date.UTC(2021,7,13),5699.00,\"购买1件,当前价:6599.00,优惠券：满4000减900\"],[Date.UTC(2021,7,14),6599.00,\"\"],[Date.UTC(2021,7,15),5999.00,\"购买1件,当前价:6599.00,优惠券：满4000减600\"],[Date.UTC(2021,7,16),5999.00,\"购买1件,当前价:6599.00,优惠券：满4000减600\"],[Date.UTC(2021,7,17),5999.00,\"购买1件,当前价:6599.00,优惠券：满4000减600\"],[Date.UTC(2021,7,18),5699.00,\"购买1件,当前价:6299.00,优惠券：满4000减600\"],[Date.UTC(2021,7,19),5999.00,\"购买1件,当前价:6599.00,优惠券：满4000减600\"],[Date.UTC(2021,7,20),5999.00,\"购买1件,当前价:6599.00,优惠券：满4000减600\"],[Date.UTC(2021,7,21),5999.00,\"购买1件,当前价:6599.00,优惠券：满4000减600\"],[Date.UTC(2021,7,22),5999.00,\"购买1件,当前价:6599.00,优惠券：满4000减600\"],[Date.UTC(2021,7,23),5999.00,\"购买1件,当前价:6599.00,优惠券：满4000减600\"],[Date.UTC(2021,7,24),5999.00,\"购买1件,当前价:6599.00,优惠券：满4000减600\"],[Date.UTC(2021,7,25),5999.00,\"购买1件,当前价:6599.00,优惠券：满4000减600\"],[Date.UTC(2021,7,26),5999.00,\"购买1件,当前价:6599.00,优惠券：满4000减600\"],[Date.UTC(2021,7,27),5999.00,\"购买1件,当前价:6599.00,优惠券：满4000减600\"],[Date.UTC(2021,7,28),5999.00,\"购买1件,当前价:6599.00,优惠券：满4000减600\"],[Date.UTC(2021,7,29),5999.00,\"购买1件,当前价:6599.00,优惠券：满4000减600\"],[Date.UTC(2021,7,30),5999.00,\"购买1件,当前价:6599.00,优惠券：满4000减600\"],[Date.UTC(2021,7,31),5999.00,\"购买1件,当前价:6599.00,优惠券：满4000减600\"],[Date.UTC(2021,8,1),5999.00,\"购买1件,当前价:6599.00,优惠券：满4000减600\"],[Date.UTC(2021,8,2),5999.00,\"购买1件,当前价:6599.00,优惠券：满4000减600\"],[Date.UTC(2021,8,3),5999.00,\"购买1件,当前价:6599.00,优惠券：满4000减600\"],[Date.UTC(2021,8,4),5999.00,\"购买1件,当前价:6599.00,优惠券：满4000减600\"],[Date.UTC(2021,8,5),5999.00,\"购买1件,当前价:6599.00,优惠券：满4000减600\"],[Date.UTC(2021,8,6),5999.00,\"购买1件,当前价:6599.00,优惠券：满4000减600\"],[Date.UTC(2021,8,7),5999.00,\"购买1件,当前价:6599.00,优惠券：满4000减600\"],[Date.UTC(2021,8,8),5999.00,\"购买1件,当前价:6599.00,优惠券：满4000减600\"],[Date.UTC(2021,8,9),5799.00,\"购买1件,当前价:6399.00,优惠券：满4000减600\"],[Date.UTC(2021,8,10),5999.00,\"购买1件,当前价:6599.00,优惠券：满4000减600\"],[Date.UTC(2021,8,11),5999.00,\"购买1件,当前价:6599.00,优惠券：满4000减600\"],[Date.UTC(2021,8,12),5999.00,\"购买1件,当前价:6599.00,优惠券：满4000减600\"],[Date.UTC(2021,8,13),5999.00,\"购买1件,当前价:6599.00,优惠券：满4000减600\"],[Date.UTC(2021,8,14),5999.00,\"5999元包邮\"],[Date.UTC(2021,8,15),5599.00,\"购买1件,当前价:6199.00,优惠券：满4000减600\"],[Date.UTC(2021,8,16),5599.00,\"购买1件,当前价:6199.00,优惠券：满4000减600\"],[Date.UTC(2021,8,17),5599.00,\"购买1件,当前价:6199.00,优惠券：满4000减600\"],[Date.UTC(2021,8,18),5599.00,\"购买1件,当前价:6199.00,优惠券：满4000减600\"],[Date.UTC(2021,8,19),5599.00,\"购买1件,当前价:6199.00,优惠券：满4000减600\"],[Date.UTC(2021,8,20),5599.00,\"购买1件,当前价:6199.00,优惠券：满4000减600\"],[Date.UTC(2021,8,21),5599.00,\"购买1件,当前价:6199.00,优惠券：满4000减600\"],[Date.UTC(2021,8,22),5599.00,\"\"],[Date.UTC(2021,8,23),5539.00,\"5539元\"],[Date.UTC(2021,8,24),5599.00,\"\"],[Date.UTC(2021,8,25),5599.00,\"\"],[Date.UTC(2021,8,26),5599.00,\"5599元\"],[Date.UTC(2021,8,27),5299.00,\"购买1件,当前价:5599.00,优惠券：满4000减300\"],[Date.UTC(2021,8,28),5299.00,\"购买1件,当前价:5599.00,优惠券：满4000减300\"],[Date.UTC(2021,8,29),5299.00,\"购买1件,当前价:5599.00,优惠券：满4000减300\"],[Date.UTC(2021,8,30),5299.00,\"购买1件,当前价:5599.00,优惠券：满4000减300\"],[Date.UTC(2021,9,1),5299.00,\"购买1件,当前价:5599.00,优惠券：满4000减300\"],[Date.UTC(2021,9,2),5299.00,\"购买1件,当前价:5599.00,优惠券：满4000减300\"],[Date.UTC(2021,9,3),5299.00,\"购买1件,当前价:5599.00,优惠券：满4000减300\"],[Date.UTC(2021,9,4),5299.00,\"购买1件,当前价:5599.00,优惠券：满4000减300\"],[Date.UTC(2021,9,5),5299.00,\"购买1件,当前价:5599.00,优惠券：满4000减300\"],[Date.UTC(2021,9,6),5299.00,\"购买1件,当前价:5599.00,优惠券：满4000减300\"],[Date.UTC(2021,9,7),5299.00,\"购买1件,当前价:5599.00,优惠券：满4000减300\"],[Date.UTC(2021,9,8),5299.00,\"购买1件,当前价:5599.00,优惠券：满4000减300\"],[Date.UTC(2021,9,9),5299.00,\"购买1件,当前价:5599.00,优惠券：满4000减300\"],[Date.UTC(2021,9,10),5299.00,\"购买1件,当前价:5599.00,优惠券：满4000减300\"],[Date.UTC(2021,9,11),5299.00,\"购买1件,当前价:5599.00,优惠券：满4000减300\"],[Date.UTC(2021,9,12),5299.00,\"购买1件,当前价:5599.00,优惠券：满4000减300\"],[Date.UTC(2021,9,13),5299.00,\"购买1件,当前价:5599.00,优惠券：满4000减300\"],[Date.UTC(2021,9,14),5299.00,\"购买1件,当前价:5599.00,优惠券：满4000减300\"],[Date.UTC(2021,9,15),5299.00,\"购买1件,当前价:5599.00,优惠券：满4000减300\"],[Date.UTC(2021,9,16),5299.00,\"购买1件,当前价:5599.00,优惠券：满4000减300\"],[Date.UTC(2021,9,17),5299.00,\"购买1件,当前价:5599.00,优惠券：满4000减300\"],[Date.UTC(2021,9,18),5299.00,\"购买1件,当前价:5599.00,优惠券：满4000减300\"],[Date.UTC(2021,9,19),5299.00,\"购买1件,当前价:5599.00,优惠券：满4000减300\"],[Date.UTC(2021,9,20),5299.00,\"购买1件,当前价:5599.00,优惠券：满4000减300\"],[Date.UTC(2021,9,21),5299.00,\"购买1件,当前价:5599.00,优惠券：满4000减300\"],[Date.UTC(2021,9,22),5299.00,\"购买1件,当前价:5599.00,优惠券：满4000减300\"],[Date.UTC(2021,9,23),5399.0,\"\"],[Date.UTC(2021,9,24),5399.00,\"\"],[Date.UTC(2021,9,25),5399.00,\"\"],[Date.UTC(2021,9,26),5399.00,\"\"],[Date.UTC(2021,9,27),5399.00,\"\"],[Date.UTC(2021,9,28),5399.00,\"\"],[Date.UTC(2021,9,29),5399.00,\"\"],[Date.UTC(2021,9,30),5399.00,\"\"],[Date.UTC(2021,9,30),4999.00,\"购买1件,当前价:5399.00,可叠加优惠券2：满4000减400\"],[Date.UTC(2021,10,1),4999.00,\"购买1件,当前价:5399.00,可叠加优惠券2：满5000减400\"],[Date.UTC(2021,10,2),5099.0,\"\"],[Date.UTC(2021,10,3),5099.00,\"\"],[Date.UTC(2021,10,4),4999.00,\"4999元\"],[Date.UTC(2021,10,5),4999.00,\"购买1件,当前价:5099.00,优惠券：满4000减100\"],[Date.UTC(2021,10,6),5099.00,\"\"],[Date.UTC(2021,10,7),5099.00,\"\"],[Date.UTC(2021,10,8),4909.00,\"4909元\"],[Date.UTC(2021,10,9),4799.00,\"4799元包邮（需用券）\"],[Date.UTC(2021,10,10),4799.00,\"购买1件,当前价:5099.00,优惠券：满4000减300\"],[Date.UTC(2021,10,11),4799.00,\"购买1件,当前价:5099.00,优惠券：满4000减300\"],[Date.UTC(2021,10,12),5399.0,\"\"],[Date.UTC(2021,10,13),5399.00,\"\"],[Date.UTC(2021,10,14),5399.00,\"5399元\"],[Date.UTC(2021,10,15),5399.00,\"\"],[Date.UTC(2021,10,16),5399.00,\"\"],[Date.UTC(2021,10,17),5399.00,\"5399元\"],[Date.UTC(2021,10,18),5399.00,\"\"],[Date.UTC(2021,10,19),5399.00,\"\"],[Date.UTC(2021,10,20),5399.00,\"5399元\"],[Date.UTC(2021,10,21),5399.00,\"\"],[Date.UTC(2021,10,22),5399.00,\"\"],[Date.UTC(2021,10,23),4999.00,\"\"],[Date.UTC(2021,10,24),5199.0,\"\"],[Date.UTC(2021,10,25),5199.00,\"\"],[Date.UTC(2021,10,26),5199.00,\"\"],[Date.UTC(2021,10,27),5199.00,\"\"],[Date.UTC(2021,10,28),5199.00,\"5199元\"],[Date.UTC(2021,10,29),4899.0,\"\"],[Date.UTC(2021,10,30),4899.00,\"4899元\"],[Date.UTC(2021,11,1),4899.00,\"\"],[Date.UTC(2021,11,2),4899.00,\"\"],[Date.UTC(2021,11,3),4899.00,\"\"],[Date.UTC(2021,11,4),4899.00,\"\"],[Date.UTC(2021,11,5),4899.00,\"\"],[Date.UTC(2021,11,6),4899.00,\"4899元\"],[Date.UTC(2021,11,7),4899.00,\"\"],[Date.UTC(2021,11,8),5199.0,\"\"],[Date.UTC(2021,11,9),5199.00,\"\"],[Date.UTC(2021,11,10),5199.00,\"\"],[Date.UTC(2021,11,11),4659.00,\"4659元\"],[Date.UTC(2021,11,12),4579.00,\"4579元（需用券）\"],[Date.UTC(2021,11,13),4899.0,\"\"],[Date.UTC(2021,11,14),5199.0,\"\"],[Date.UTC(2021,11,15),5199.0,\"\"],[Date.UTC(2021,11,16),5199.0,\"\"],[Date.UTC(2021,11,17),5199.0,\"\"],[Date.UTC(2021,11,18),5199.0,\"\"],[Date.UTC(2021,11,19),5199.0,\"\"],[Date.UTC(2021,11,20),5199.0,\"\"],[Date.UTC(2021,11,21),5199.0,\"\"],[Date.UTC(2021,11,22),5199.0,\"\"],[Date.UTC(2021,11,23),5199.0000,\"\"],[Date.UTC(2021,11,24),5196.00,\"5196元\"],[Date.UTC(2021,11,25),5199.00,\"\"],[Date.UTC(2021,11,26),5199.00,\"\"],[Date.UTC(2021,11,27),5199.00,\"\"],[Date.UTC(2021,11,28),5199.00,\"\"],[Date.UTC(2021,11,29),5199.00,\"\"],[Date.UTC(2021,11,30),5199.00,\"\"],[Date.UTC(2021,11,30),4699.00,\"购买1件,当前价:5199.00,可叠加优惠券2：满4000减500\"],[Date.UTC(2021,12,1),4459.00,\"4459元包邮（需用券）\"],[Date.UTC(2021,12,2),5199.00,\"\"],[Date.UTC(2021,12,3),5199.00,\"\"],[Date.UTC(2021,12,4),5199.00,\"\"],[Date.UTC(2021,12,5),5199.00,\"\"],[Date.UTC(2021,12,6),5199.00,\"\"],[Date.UTC(2021,12,7),5199.00,\"\"],[Date.UTC(2021,12,8),5199.00,\"\"],[Date.UTC(2021,12,9),4899.0,\"\"],[Date.UTC(2021,12,10),4899.00,\"\"],[Date.UTC(2021,12,11),4899.00,\"\"],[Date.UTC(2021,12,12),4899.00,\"\"],[Date.UTC(2021,12,13),5199.00,\"\"],[Date.UTC(2021,12,14),5199.00,\"\"],[Date.UTC(2021,12,15),5199.00,\"\"],[Date.UTC(2021,12,16),5199.00,\"\"],[Date.UTC(2021,12,17),4899.00,\"4899元\"],[Date.UTC(2021,12,18),4899.0000,\"\"],[Date.UTC(2021,12,19),4899.0000,\"\"],[Date.UTC(2021,12,20),4899.0000,\"\"],[Date.UTC(2021,12,21),5149.00,\"5149元\"],[Date.UTC(2021,12,22),5199.00,\"\"],[Date.UTC(2021,12,23),5199.00,\"\"],[Date.UTC(2021,12,24),5199.00,\"\"],[Date.UTC(2021,12,25),5199.00,\"\"],[Date.UTC(2021,12,26),5199.00,\"\"],[Date.UTC(2021,12,27),5199.00,\"\"],[Date.UTC(2021,12,28),5199.00,\"\"],[Date.UTC(2021,12,29),5199.00,\"\"],[Date.UTC(2021,12,30),5199.00,\"\"],[Date.UTC(2021,12,31),4799.00,\"购买1件,当前价:5199.00,可叠加优惠券2：满3880减400\"],[Date.UTC(2022,1,1),4799.00,\"购买1件,当前价:5199.00,可叠加优惠券2：满3880减400\"],[Date.UTC(2022,1,2),4799.00,\"购买1件,当前价:5199.00,可叠加优惠券2：满3880减400\"],[Date.UTC(2022,1,3),5199.00,\"\"],[Date.UTC(2022,1,4),5199.00,\"\"],[Date.UTC(2022,1,5),5199.00,\"\"],[Date.UTC(2022,1,6),5199.00,\"\"],[Date.UTC(2022,1,7),5199.00,\"\"],[Date.UTC(2022,1,8),5199.00,\"\"],[Date.UTC(2022,1,9),5199.00,\"4599元\"],[Date.UTC(2022,1,10),5199.00,\"\"],[Date.UTC(2022,1,11),4599.00,\"4599元 包邮（需用券）\"],[Date.UTC(2022,1,12),5199.00,\"\"],[Date.UTC(2022,1,13),5199.00,\"4599元\"],[Date.UTC(2022,1,14),5199.00,\"\"],[Date.UTC(2022,1,15),5199.00,\"\"],[Date.UTC(2022,1,16),5199.00,\"\"],[Date.UTC(2022,1,17),5199.00,\"\"],[Date.UTC(2022,1,18),5199.00,\"\"],[Date.UTC(2022,1,19),5199.00,\"\"],[Date.UTC(2022,1,20),5199.00,\"\"],[Date.UTC(2022,1,21),5199.00,\"\"],[Date.UTC(2022,1,22),5199.00,\"\"],[Date.UTC(2022,1,23),5199.00,\"\"],[Date.UTC(2022,1,24),5199.00,\"\"],[Date.UTC(2022,1,25),5199.00,\"\"],[Date.UTC(2022,1,26),5199.00,\"\"],[Date.UTC(2022,1,27),5199.00,\"\"],[Date.UTC(2022,1,28),5199.00,\"\"],[Date.UTC(2022,2,1),5199.00,\"\"],[Date.UTC(2022,2,2),5199.00,\"\"],[Date.UTC(2022,2,3),5199.00,\"\"],[Date.UTC(2022,2,4),5199.00,\"\"],[Date.UTC(2022,2,5),5199.00,\"\"],[Date.UTC(2022,2,6),5199.00,\"\"],[Date.UTC(2022,2,7),5199.00,\"\"],[Date.UTC(2022,2,8),5199.00,\"\"],[Date.UTC(2022,2,9),5199.00,\"\"],[Date.UTC(2022,2,10),5199.00,\"\"],[Date.UTC(2022,2,11),5199.00,\"5199元\"],[Date.UTC(2022,2,12),5199.00,\"\"],[Date.UTC(2022,2,13),5199.00,\"\"],[Date.UTC(2022,2,14),5199.00,\"\"],[Date.UTC(2022,2,15),5199.00,\"\"],[Date.UTC(2022,2,16),5199.00,\"\"],[Date.UTC(2022,2,17),5199.00,\"\"],[Date.UTC(2022,2,18),5199.00,\"\"],[Date.UTC(2022,2,19),5199.00,\"\"],[Date.UTC(2022,2,20),5199.00,\"\"],[Date.UTC(2022,2,21),5199.00,\"\"],[Date.UTC(2022,2,22),5199.00,\"\"],[Date.UTC(2022,2,23),5199.00,\"\"],[Date.UTC(2022,2,24),5199.00,\"\"],[Date.UTC(2022,2,25),5199.00,\"\"],[Date.UTC(2022,2,26),5199.00,\"\"],[Date.UTC(2022,2,27),5199.00,\"\"],[Date.UTC(2022,2,28),4799.00,\"4799元\"],[Date.UTC(2022,2,28),4799.0000,\"\"],[Date.UTC(2022,2,28),4799.0000,\"\"],[Date.UTC(2022,2,28),4799.0000,\"\"],[Date.UTC(2022,3,1),5199.00,\"\"],[Date.UTC(2022,3,2),5199.00,\"\"],[Date.UTC(2022,3,3),5199.00,\"\"],[Date.UTC(2022,3,4),5199.00,\"\"],[Date.UTC(2022,3,5),5199.00,\"\"],[Date.UTC(2022,3,6),5199.00,\"\"]"
res = eval(jiagequshi.replace('Date.UTC',''))
print(len(res))
for re in res:
    print(len(re))
print(res)