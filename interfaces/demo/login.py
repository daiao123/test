# -*- coding: utf-8 -*-
from requests.api import get

params = {
    'account':'admin',
    'pwd':'660B8D2D5359FF6F94F8D3345698F88C'
}

cookies = {
    'JSESSIONID':'9F212E994E8174481170EC4727A77D62'
}
response = get(url='http://192.168.1.25:8080/recruit.students/login/in', params=params, cookies=cookies)

print(response.text)

print(response.status_code)
print(response.headers)
#print(response.cookies.get('Set-Cookie'))


