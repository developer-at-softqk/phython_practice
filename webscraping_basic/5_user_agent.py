import requests
url = "http://nadocoding.tistory.com"
# user agent string 검색 후 https://www.whatismybrowser.com/detect/what-is-my-user-agent 페이지에서 내 agent 정보를 header에 넣어준다
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"}
res = requests.get(url, headers)
res.raise_for_status() # 문제가 생겼을떄 오류를 내뱉고 오류 발생시킴

with open("nadocoding.html", "w", encoding="utf8") as f:
    f.write(res.text)