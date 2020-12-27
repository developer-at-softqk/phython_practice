# beautifulsoup4, lxml

import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/weekday.nhn"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml") # lxml파서로 res.text를 soup으로 변경
# print(soup.title)
# print(soup.title.get_text())
# print(soup.a) #soup 객체에서 처음 발견된 첫번째 a 정보 출력
# print(soup.a.attrs) # a element 의 속성 정보 출력
# print(soup.a["href"]) # element 의 속성의 값 정보 출력

# print(soup.find("a", attrs={"class":"Nbtn_upload"})) # class=Nbtn_upload 인 a element를 찾아줘
# print(soup.find(attrs={"class":"Nbtn_upload"})) # class=Nbtn_upload 인 어떤 element를 찾아줘

# print(soup.find("li", attrs={"class":"rank01"}))
# rank1 = soup.find("li", attrs={"class":"rank01"})
# print(rank1.a.get_text())
# print(rank1.next_sibling)
""" 형제태그 """
# rank2 = rank1.next_sibling.next_sibling
# rank3 = rank2.next_sibling.next_sibling
# print(rank3.a.get_text())
# rank2 = rank3.previous_sibling.previous_sibling
# print(rank2.a.get_text())

""" 부모태그 """
# print(rank1.parent)

# rank2 = rank1.find_next_sibling("li")
# # print(rank2.a.get_text())
# rank3 = rank2.find_next_sibling("li")
# # print(rank3.a.get_text())
# rank2 = rank3.find_previous_sibling("li")
# print(rank2.a.get_text())

# print(rank1.find_next_siblings("li"))

webtoon = soup.find("a", text="참교육-9화")
print(webtoon)

# <a onclick="nclk_v2(event,'rnk*p.cont','758037','1')" href="/webtoon/detail.nhn?titleId=758037&amp;no=9" title="참교육-9화">참교육-9화</a>