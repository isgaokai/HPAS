import re

from django.shortcuts import render

# Create your views here.
import json
from random import randrange

from django.http import HttpResponse
from rest_framework.views import APIView

from pyecharts.charts import Bar, Line
from pyecharts import options as opts


# Create your views here.
from Bot.Bot.contentBot import history_price_bot
from Bot.Bot.dataBot import data_treat_bot


def response_as_json(data):

    json_str = json.dumps(data)
    response = HttpResponse(
        json_str,
        content_type="application/json",
    )
    response["Access-Control-Allow-Origin"] = "*"

    return response


def json_response(data, code=200):

    data = {
        "code": code,
        "msg": "success",
        "data": data,
    }
    return response_as_json(data)


def json_error(error_string="error", code=500, **kwargs):

    data = {
        "code": code,
        "msg": error_string,
        "data": {}
    }
    data.update(kwargs)
    return response_as_json(data)


JsonResponse = json_response
JsonError = json_error


def bar_base(history_url):
    # 进行数据获取
    item_title, item_lower_price, item_lower_price_yh, item_price_trend = history_price_bot(history_url)
    # 判断是否获取到正确数据
    if not item_title or not item_lower_price_yh or not item_lower_price or not item_price_trend:
        return 'false'
    # 对获取到到数据进行处理
    date_, price_, tip_ = data_treat_bot(item_price_trend)
    # 自定义提示点数据
    tip_data = []
    # 对提示点进行数据添加
    for index in range(len(tip_)):
        if not tip_[index]:
            continue
        tip_data.append(opts.MarkPointItem(
            # 显示
            name=str(date_[index]) + '\n' + str(price_[index]) + '\n' + tip_[index],
            # 坐标
            coord=[date_[index], price_[index]],
            # 图形
            symbol='roundRect',
            # 大小
            symbol_size=[2.5, 2.5]
        ))

    c = (
        # 初始化Line 设置宽度
        Line(init_opts=opts.InitOpts(width="1500px"))
        # 添加x轴
        .add_xaxis(date_)
        # 添加y轴
        .add_yaxis(y_axis=price_, series_name=item_title, is_step=False,
                   # 添加自定义提示点
                   markpoint_opts=opts.MarkPointOpts(
                       data=tip_data
                   ))
        # 设置全局配置
        .set_global_opts(
            yaxis_opts=opts.AxisOpts(axispointer_opts={"rotate":45}),
            #              # 横轴放大缩小功能
            #              datazoom_opts=opts.DataZoomOpts()
            )
        # 进行渲染
        .dump_options_with_quotes()
    )
    return c


class ChartView(APIView):
    # 数据入口
    def get(self, request, *args, **kwargs):

        # url正则
        uPattern = re.compile('(http|https):\/\/([\w.]+\/?)\S*')

        # 获取接收的url
        history_key = request.GET.get('history_key','null')
        # 未通过验证
        if not uPattern.search(history_key):
            return JsonResponse(json.loads('false'))
        print(history_key)
        return JsonResponse(json.loads(bar_base(history_key)))


class IndexView(APIView):

    def get(self, request, *args, **kwargs):
        return HttpResponse(content=open("./templates/index.html").read())