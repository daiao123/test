import pytest

def test_04_func():
    print("函数")

class Testlogin:

    # @pytest.mark.run(order=3)
    # @pytest.mark.smoke
    def test_03_inter(self, my_fixture):
        print("接口测试")

