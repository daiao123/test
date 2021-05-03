# -*- coding: utf-8 -*-
from json import loads

from requests.api import post

json = [{
        "id": "5671",
        "recruitStartTime": "2021-04-01",
        "recruitEndTime": "2021-04-09",
        "isStudentRecruitTime": "1"
    }]
cookies = {
    'JSESSIONID':'9F212E994E8174481170EC4727A77D62'
}
response = post('http://192.168.1.25:8080/recruit.students/school/manage/setStudentRecruitTime', json=json, cookies=cookies)

text = response.text
print(text)

print(response.status_code)

response_text = loads(text)['message']

