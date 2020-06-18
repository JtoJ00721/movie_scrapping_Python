# 제목
# 내용
# 작성일자
# 작성자

import requests
from bs4 import BeautifulSoup

cnt = 0

for page in range(1,6):
    list_url = 'http://news.sarangbang.com/bbs.html?tab=story&keyword=&p={}'.format(page)
    resp = requests.get(list_url)

if resp.status_code != 200:
    print('없지롱')

    soup = BeautifulSoup(resp.text, 'html.parser')
    board_list = soup.select('tbody#bbsResult > tr > td > a:not(.name_more)')

for i, href in enumerate(board_list):
    # print(i, href)
    cnt += 1
    print('http://news.sarangbang.com' + href['href'])

    print(board_list)

    # 1건의 개시글의 제목, 내용, 작성자, 작성일자를 수집하는 코드
    url = 'http://news.sarangbang.com' + href['href']

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

print('사랑방 부동산에서 {}건의 개시글을 수집하였습니다'.format(cnt))
