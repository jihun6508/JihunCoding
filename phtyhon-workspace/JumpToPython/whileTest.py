"""testList = [1,2,3,4]
for i in testList:
    print(i)
a = [(1,2), (3,4), (5,6)]
for (first, last) in a:
    print(first, last)

b = [(1,2,3), (3,4,5), (5,6,7)]
for (first, snd, last) in b:
    print(first,snd,last)
"""

"""
treehit = 0
while treehit < 10:
    treehit +=1
    print(str(treehit) + "회 나무를 때렸습니다.")
    if treehit == 10:
        print("나무가 넘어갔습니다")"""
"""coffee = 10
money = 300
while money:
    coffee = coffee - 1
    print ("커피를 팔았습니다. 커피가 %d잔 남았습니다."%coffee)
    if coffee == 0:
        print("커피가 다 팔렸습니다")
        break"""
'''[90, 25, 67, 45, 80] 60점 이상이면 합격, n번 학생 축하합니다.'''

'''cofffee2 = 10
while True:
    money =  int(input("돈을 넣어주세요: "))
    if money == 300:
        print("커피를 줍ㄴ디ㅏ.")
        cofffee2 -= 1
    elif money > 300:
        print ("커피를 주고 잔액을 반환합니다.")
        change = money - 300
        print ("잔액: " + str(change) + "원")
        cofffee2 -= 1
    elif money < 300:
        print("금액이 모자랍니다. %d원을 반환합니다." %money)
    if cofffee2 == 0:
        print("커피가 다 떨어졌습니다.")
        break'''
"""
a = 0
while a <10:
    a +=1
    if a%2 == 1:
        print(a)"""

# marks = [90,25,67,45,80]
"""
num = 0
for i in marks:
    num += 1
    if i > 60:
        print(str(num) + "번: 합격")
    else: continue
print(range(len(marks)))
"""
# for number in range(len(marks)):
#     if marks[number] > 60:
#         print(str(number+1) + "번: 합격")
#     else : continue
#구구단
for i in range(2,10):
    for a in range(1,10):
        print ("%d x %d = %d" %(i,a,i*a))

# a = 1
# b = 0
# while a <= 1000:
#     if a%3 == 0:
#         b += a
#     a += 1
# print(b)

# a = 0
# while a < 5:
#     a += 1
#     print("*"*a)

# for a in range(1,101):
#     print(a)
#     a +=1

# midlleTestScore = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
# sum = 0
# for n in midlleTestScore:
#     sum += n
# average = sum / len(midlleTestScore)
# print(average)

#리스트 내포
# numbers = [1, 2, 3, 4, 5]
# result = []
# for n in numbers:
#     if n % 2 == 1:
#         result.append(n*2)
# result = [2*n for n in numbers if n%2 == 1]
# print(result)