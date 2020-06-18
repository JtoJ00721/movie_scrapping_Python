import requests
from bs4 import BeautifulSoup

cnt = 0

for i in range(1, 4):
    url = 'https://news.daum.net/breakingnews/?page={}' .format(i)
    print(url)

    resp = requests.get(url)
    url_list = soup.select('ul.list_allnews a.link.txt')

    for j in url_list:
        cnt += 1
        url = j['href']
        soup = BeautifulSoup(resp.text, 'html.parser')
        title = soup.select('h3.tit_view')
        contents = soup.select('div#harmonyContainer p')

        text = ''
        for k in contents:
            text += k.text

        print('=================================================================')
        print(title[0].text)
        print('-----------------------------------------------------------------')
        print(text)

print('{}건의 뉴스기사 수집'.format(cnt))