import requests
from bs4 import BeautifulSoup

url = 'https://news.v.daum.net/v/20200616091314577'
resp = requests.get(url)

if resp.status_code == 200:
    print('Success')
else:
    print('Wrong')

soup = BeautifulSoup(resp.text, 'html.parser')
title = soup.select('h3.tit_view')
content = soup.select('div#harmonyContainer')
contents = soup.select('div#harmonyContainer p')


print(title[0].text)
print(content[0].text.strip())
print(contents)
print('===========================================================')

text = ''
for i in contents:
    text += i

print(text)
