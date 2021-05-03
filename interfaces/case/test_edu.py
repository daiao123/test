from json import loads

import pytest
from requests.api import get
from requests.api import post

from dao.MySQLHelper import MySQLHelper
from utils.Config import Config
from utils.Logger import Logger

logger = Logger('TestEdu').getlog()
file = './conf/config.ini'


@pytest.fixture(scope='class')
def get_db():
    config = Config(file)
    my = MySQLHelper()
    my.host = config.get_value(file, 'mysql', 'host')
    my.user = config.get_value(file, 'mysql', 'user')
    my.password = config.get_value(file, 'mysql', 'password')
    my.database = config.get_value(file, 'mysql', 'database')
    my.port = int(config.get_value(file, 'mysql', 'port'))
    return my


@pytest.fixture(scope='class')
def init_config():
    config = Config(file)
    configs = {
        'url':config.get_value(file, 'base', 'url'),
        'port':config.get_value(file, 'base', 'port'),
        'project_name':config.get_value(file, 'base', 'project_name'),
    }
    return configs

@pytest.fixture(scope='class')
def init_cookies():
    config = Config(file)
    cookie = {
        'JSESSIONID':config.get_value(file, 'cookies', 'JSESSIONID')
    }
    return cookie    


class TestEdu():

    def test_login(self, get_db, init_config,init_cookies):
        config = init_config
        db = get_db
        cookie = init_cookies

        sql = "select * from t_login_account where f_school_id=1"
        
        result = db.select(sql, 'one')
        logger.info(result)
        
        params = {
            'account':'%s' % result[2],
            'pwd':'%s' % result[3]
        }
        
        response = get(url='http://%s:%s/%s/login/in' %(config['url'],config['port'],config['project_name']), params=params, cookies=cookie) 
        logger.info(response)
        assert response.status_code == 200  # 断言

    def tes_addschool(self):
        data = [('schoolName', 'caichang888'), ('listSchoolType[0].id', 2), ('canRecruit', 1), ('remark', 'hehe')]
        
        response = post('http://192.168.1.25:8080/recruit.students/school/manage/addSchoolInfo', data=data, cookies=self.cookies)
        
        text = response.text
        
        response_text = loads(text)['message']
        assert response_text == '学校创建成功'

    def tes_setstudentrecruilttime(self):

        json = [{
                "id": "5671",
                "recruitStartTime": "2021-04-01",
                "recruitEndTime": "2021-04-09",
                "isStudentRecruitTime": "1"
            }]

        response = post('http://192.168.1.25:8080/recruit.students/school/manage/setStudentRecruitTime', json=json, cookies=self.cookies)
        
        text = response.text
        
        response_text = loads(text)['code']
        assert response_text == 1
