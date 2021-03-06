import requests
from bs4 import BeautifulSoup


url = 'https://news.v.daum.net/v/20200615143137572'
# url사이트에 get방식으로 requests를 하면
# return으로 사이트의 html  code를 전달
resp = requests.get(url)

if resp.status_code == 200:
    resp.headers
else:
    print('잘못된 url입니다. 다시 입력해 주세요.')


soup = BeautifulSoup(resp.text, 'html.parser')
title = soup.find('h3', id='tit_view')
contents = soup.find('div', id='jFWk6VhoTS')

print(title.text)
print(resp.text)
print(contents.text.strip())
