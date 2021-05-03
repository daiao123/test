import time

import pytest


class Testlogin:
    # age = 21

    def setup_class(self):
        print('\n在每个类执行前的初始化工作：比如：创建日志对象，创建数据库的连接，创建接口的请求对象')

    # 在每个用例之前执行一次
    def setup(self):
        print('\n在执行用例之前初始化代码：打开浏览器，加载网页')

    def test_01_login(self):
        print("第一个pytest")

    # @pytest.mark.run(order=2)
    # @pytest.mark.smoke
    def test_02_add(self):
        print("第二个pytest")
        # assert 1 == 2

    # @pytest.mark.usermanage
    # @pytest.mark.skipif(age > 18, reason="年龄太大了")
    # def test_03_add(self):
    #     print("第三个pytest")

    # @pytest.mark.run(order=1)
    # @pytest.mark.skip(reason="不想执行")
    # def test_04_add(self):
    #     print("第四个pytest")

    def teardown(self):
        print('\n在执行用例之后的扫尾工作：关闭浏览器，关闭网页')

    def teardown_class(self):
        print('\n在每个类执行后的扫尾工作：比如：销毁日志对象，销毁数据库的连接，销毁接口的请求对象')

