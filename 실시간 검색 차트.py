import requests as rq
from bs4 import BeautifulSoup as bs

req = rq.get("http://datalab.naver.com/")
html = req.text

if req.status_code == 200:
    soup = bs(html,'html.parser')
    keyword_rank = soup.find('div',{'class':'keyword_rank select_date'})

    print(keyword_rank.find('strong',{'class':'rank_title v2'}).text)
    rank_list = keyword_rank.find('ul',{'class':'rank_list'}).find_all('a')
    for rank in rank_list:
        num = rank.find('em').text
        title = rank.find('span').text
        print(num,title)

else:
    print("HTTP 통신에 실패하였습니다.")
