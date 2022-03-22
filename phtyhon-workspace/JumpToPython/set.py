asia = {'한국', '중국','일본'} #집합(set)
asia.add("베트남") #add는 한개의 값 추가
asia.add("중국") # 중복값은 추가되지 않음
asia.remove("일본") # 해당값 제거
asia.update({"한국", "홍콩", "태국"})

print(asia)

lol = [[1,2,3], [4,5], [6,7,8,9]]
print(lol)

for sub in lol:
    for item in sub:
        print(item, end=" ")
    print()

#실행결과
# 1 2 3 
# 4 5 
# 6 7 8 9 
