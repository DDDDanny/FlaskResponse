# -*- coding: utf-8 -*-
# @Time    : 2020/10/22 23:12
# @Author  : DannyDong
# @File    : Result.py
# @describe: 封装处理请求结果

from flask import jsonify


class Result(object):
    def __init__(self, data=None, msg='请求成功'):
        """
        构造函数，初始化数据
        :param data: Response Data
        :param msg: Response Message
        """
        self.data = data
        self.msg = msg

    # 生产Response结果
    def create_result(self):
        pass

    # 成功
    def success(self, res):
        pass

    # 失败
    def fail(self, res):
        pass


if __name__ == '__main__':
    Result()
