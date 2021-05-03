import pytest

@pytest.fixture(scope="function")
def user_fixture(request):
    print("用户前置处理器")
    yield
    print("用户后置处理器")