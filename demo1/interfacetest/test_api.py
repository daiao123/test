import os

import pytest
import requests

from interfacetest.test_yaml import YamlUtil


class TestApi:

    @pytest.mark.parametrize('args', YamlUtil('./interfacetest/test_yaml.yaml').read_yaml())
    def test_info(self, args):
        print(args)
        url = args['request']['url']
        params = args['request']['params']
        # cooikes = args['cooikes']['JSESSIONID']
        cooikes = {
            'JSESSIONID': '6EFDC6AD8840C0E2EE5CB220B2D49296'
        }

        res = requests.get(url, params=params, cookies=cooikes)
        print(res.status_code)

    # def test_addschool(self):
    #     url = 'http://localhost:8080/recruit.students/school/manage/addSchoolInfo'
    #     data = {
    #         "schoolName": "admins",
    #         "listSchoolType[0].id": "2",
    #         "canRecruit": "1",
    #         "remark": "666"
    #     }
    #     cooikes = {
    #         "JSESSIONID": "6EFDC6AD8840C0E2EE5CB220B2D49296"
    #     }
    #
    #     res = requests.get(url, data=data, cookies=cooikes)
    #     print(res.text)
