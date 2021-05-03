# -*- coding: utf-8 -*-
from json import loads

from requests.api import post


data = [('schoolName', 'caichang888'), ('listSchoolType[0].id', 2), ('canRecruit', 1), ('remark', 'hehe')]
cookies = {
    'JSESSIONID':'9F212E994E8174481170EC4727A77D62'
}
response = post('http://192.168.1.25:8080/recruit.students/school/manage/addSchoolInfo', data=data, cookies=cookies)

text = response.text

print(response.status_code)

response_text = loads(text)['message']


