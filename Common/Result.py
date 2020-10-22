# -*- coding: utf-8 -*-
# @Time    : 2020/10/22 23:12
# @Author  : DannyDong
# @File    : Result.py
# @describe: 封装处理请求结果

from flask import jsonify


class Result(object):
    def __init__(self, **kwargs):
        pass

    # 生产Response结果
    def create_result(self):
        pass

    # 成功
    def success(self, res):
        pass

    # 失败
    def fail(self, res):
        pass
