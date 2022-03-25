#점프 투 파이썬 종합문제 15. 문자열 압축하기

InputStr = input()
ResultStr = ""
count = 1
for i in range(len(InputStr)):
    try:
        if InputStr[i] == InputStr[i+1]:
            count +=1
        else : 
            ResultStr = ResultStr + InputStr[i] + str(count)
            count = 1
    except IndexError:
        pass
#깃허브 테스트를 위한 데이터 추가
print(ResultStr)
         