import requests
from bs4 import BeautifulSoup

page = 1
cnt = 0
compare_writer = ''
break_point = False # 이중 반복문을 빠져나가기 위한 조건
while True:

    url = 'https://movie.naver.com/movie/bi/mi/pointWriteFormList.nhn?code=191436&type=after&isActualPointWriteExecute=false&isMileageSubscriptionAlready=false&isMileageSubscriptionReject=false&page={}'.format(page)
    resp = requests.get(url)

    if resp.status_code != 200:
        print('없지롱')

    soup = BeautifulSoup(resp.text, 'html.parser')
    list = soup.select('div.score_result li')

    for i, reply in enumerate(list):

        previous_writer = reply.select('div.score_reple a > span')[0].text.strip()  #작성자
        cut_index = previous_writer.find('(')
        # 네이버 영화댓글의 작성자는 닉네임(아이디***) 형식으로 되어있는데
        # 닉네임만 추출하려는 코드를 짰으나 닉네임이 없는 유저도 있었다
        # 닉네임이 없는 경우 ()안의 아이디를 사용하는 코드 작성
        if cut_index > 0:
            writer = previous_writer[:cut_index]
        else:
            writer = previous_writer

        #지금 작성자 수집
        # 네이버 영화 댔글 수집 페이지의 마지막 페이지를 계산하는 코드
        # 네이버는 1명당 후기 하나만 작성가능
        # 매 페이지의 첫번째 개시글의 작성자를 compare_writer에 저장하고
        # 매 페이지의 첫번째 작성자와 compare_writer을 비교하여 같다면 중복페이지이므로 break
        if i == 0:

            if compare_writer == writer:
                print('')
                print('')
                print('개시물 총 {}건'.format(cnt))
                print('다 수집했지롱')
                break_point = True
                break
            else:
                compare_writer = writer

        score = reply.select('div.star_score > em')[0].text.strip() #별점
        contant = reply.select('div.score_reple > p > span')[0].text.strip() #내용
        date = reply.select('div.score_reple em')[1].text.strip()[:10] #작성일자


        print('{}============================================================================================'.format(cnt + 1))
        print('작성자 : ', writer)
        print('별점 : ', score)
        print(contant)
        print('작성일자 : ', date)
        cnt += 1

    if break_point:
        break


    page += 1
