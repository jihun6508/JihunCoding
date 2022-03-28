#Q20 전방 탐색
#다음은 이메일 주소를 나타내는 정규식이다.
#이 정규식은 park@naver.com, kim@daum.net, lee@myhome.co.kr 등과 매치된다.
#긍정형 전방 탐색 기법을 사용하여 .com, .net이 아닌
#이메일 주소는 제외시키는 정규식을 작성하시오.

import re

p = re.compile(r".*[@].*[.].*$") #원래 식

p2 = re.compile(r".*[@].*[.].*") #달러 표시(끝문자열부터 탐색) 제거로 전체 값 찾아옴
a = re.compile(r"(.*[@].*[.](?=com|net))")
originalText = """
kim@daum.net
lee@myhome.co.kr
park@naver.com
aaaaa
aabbvvax
adfgag
"""
# m = p2.findall(originalText)

# print(m) #원래 결과

k = a.findall(originalText) 
print(k) #수정된 결과 