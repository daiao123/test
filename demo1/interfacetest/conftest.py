import pytest

@pytest.fixture(scope="function", params=["张三", "李四"])
def my_fixture(request):
    print("前置处理器")
    yield request.param
    print("后置处理器")