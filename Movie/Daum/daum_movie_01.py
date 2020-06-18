import requests
from bs4 import BeautifulSoup
import Movie.persistence.MongoDAO as DAO

# 객체생성
mDao = DAO.MongoDAO()

cnt = 0
page = 1
while True:
    url = 'https://movie.daum.net/moviedb/grade?movieId=126335&type=netizen&page={}'.format(page)
    resp = requests.get(url)

    if resp.status_code != 200:
        print('없지롱')
    else:
        print('있지롱')

    soup = BeautifulSoup(resp.text, 'html.parser')
    reply_list = soup.select('div.review_info')

    if len(reply_list) == 0:
        print('마지막 페이지')
        break

    print(page, 'page ***************************************************************************')
    for reply in reply_list:
        writer = reply.select('em.link_profile')[0].text.strip()
        score = reply.select('em.emph_grade')[0].text.strip()
        content = reply.select('p.desc_review')[0].text.strip()
        reg_date = reply.select('span.info_append')[0].text.strip()
        print('작성자:', writer)
        print('평점:', score)
        print('내용:', content)
        index_val = reg_date.index(',')
        print('날짜:', reg_date[:index_val])
        print('====================================================================================================')
        cnt += 1

        # MongoDB에 저장하기 위해 Dict Type으로 변환!
        data = {'content': content,
                'writer': writer,
                'score': score,
                'reg_date': reg_date}

        # 내용, 작성자, 평점, 작성일자 MongoDB에 Save
        mDao.mongo_write(data)
        
    page += 1


print('댓글 총 {}건이지롱'.format(cnt))
