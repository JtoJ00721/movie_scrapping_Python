# 다음뉴스 한 페이지에서 뉴스 기사와 내용을 수집(15건)

import requests
from bs4 import BeautifulSoup

url = 'https://news.daum.net/ranking/kkomkkom/'
resp = requests.get(url)

if resp.status_code == 200:
    print('Success')
else:
    print('Wrong')

soup = BeautifulSoup(resp.text, 'html.parser')

url_list = soup.select('ul.list_news2 a.link_txt')

for i in url_list:
    url = i['href']
    soup = BeautifulSoup(resp.text, 'html.parser')
    title = soup.select('h3.tit_view')
    contents = soup.select('div#harmonyContainer p')

    text = ''
    for j in contents:
        text += j.text

    print('=================================================================')
    print(title[0].text)
    print('-----------------------------------------------------------------')
    print(text)