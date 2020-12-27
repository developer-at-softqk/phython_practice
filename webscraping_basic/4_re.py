# 정규식

# 주민등록번호
# 901201-1111111

# 이메일 주소
# gingmee29@gmail.com

# 차량 번호
# 11가 1234
# 123가 1234

# IP 주소
# 192.168.0.1

import re
# abcd, book, desk
# ca?e
# care, cafe, case, cave
# caae, cabe, cace, cade, ...

p = re.compile("ca.e") 
# . (ca.e): 하나의 문자를 의미 > care, cafe, case (o) | caffe (x)
# ^ (^de): 문자열의 시작 > desk, destination (o) | fade (x)

# $ (se$): 문자열의 끝 > case, base (o) | face (x)

def print_match(m):
    if m: # 매칭되었을때
        print(m.group())
    else:
        print("매칭되지 않음")


m = p.match("careless") # match : 주어진 문자열의 처음부터 일치하는지 확인 //good care (x), careless (o) : 뒷부분은 상관없다.
print_match(m)
# print(m.group()) # group() : 매치되지 않으면 에러발생