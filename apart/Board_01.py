#제목
#내용
#작성일자
#작성자

import requests
from bs4 import BeautifulSoup

url = 'http://news.sarangbang.com/talk/bbs/story/163978?url=%2F%2Fnews.sarangbang.com%2Fbbs.html%3Ftab%3Dstory%26keyword%3D%25EC%259D%25B5'

resp = requests.get(url)

if resp.status_code != 200:
    print('없지롱')

soup = BeautifulSoup(resp.text, 'html.parser')

title = soup.select('h3.tit_view')[0].text.strip()
writer = soup.select('a.name_more')[0].text.strip()
reg_dt = soup.select('span.tit_cat')[1].text.strip()[:10]
contents = soup.select('div.bbs_view p')

contant = ''
for i in contents:
    contant += i.text.strip()

print('TITLE', title)
print('WRITER', writer)
print('REG', reg_dt)
print('CONTANT', content)
