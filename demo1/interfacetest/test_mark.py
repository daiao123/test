import pytest


class Testlogin:

    # @pytest.mark.parametrize("args", ['张三', '李四', '王五'])
    # def test_01_fixture(self, args):
    #     print(args)

    @pytest.mark.parametrize("args, age", [['张三', '18'], ['李四', '15'], ['王五', '26']])
    def test_01_fixture(self, args, age):
        print("名字：%s  年龄：%s" % (args, age))



