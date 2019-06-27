# -*- coding: utf-8 -*-
# @Author   : 王翔
# @JianShu  : 清风Python
# @Date     : 2019/6/27 22:14
# @Software : PyCharm
# @version  ：Python 3.7.3
# @File     : views.py

from django.http import HttpResponse

def index(requst):
    html = "<h3>Hello World...</h3>"
    return HttpResponse(html)

