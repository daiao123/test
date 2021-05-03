import os

import  pytest

if __name__ == '__main__':
    # pytest.main(['-vs', './pytestcs/test_login.py', '-n=2', '--reruns=2'])
    # pytest.main(['-vs', './pytestcs/test_login.py', '-n=2', '--maxfail=2'])
    # pytest.main(['-vs', './pytestcs/test_login.py', '-n=2', '-k=add'])
    # pytest.main(['-vs', './interfacetest/test_inter.py::test_04_func'])
    # pytest.main(['-vs', './interfacetest/test_inter.py::Testlogin::test_03_inter'])
    pytest.main()
    os.system('allure generate ./temp -o ./report --clean')