TestScore = int(input("점수를 입력하세요?>> "))

if TestScore >= 90:
    print("학점은 A학점 입니다")
elif TestScore >= 80:
    print("학점은 B학점 입니다")
elif TestScore >= 70:
    print("학점은 C학점 입니다")
elif TestScore >= 60:
    print("학점은 D학점 입니다")
elif TestScore < 60:
    print("학점은 F학점 입니다")
else:
    pass

Score = ["A","B","C","D","F"]
resultScore = ""
# if TestScore >= 90:
#     resultScore = Score[0]
# elif TestScore >= 80:
#     resultScore = Score[1]
# elif TestScore >= 70:
#     resultScore = Score[2]
# elif TestScore >= 60:
#     resultScore = Score[3]
# elif TestScore < 60:
#     resultScore = Score[4]
# else:
#     pass
# print(f"학점은 {resultScore} 입니다.")

t = 90
for i in Score:
    if TestScore >= t:
        print(f"학점은 {i} 입니다.")
        break
    t-=10

# number = [1,2,3,4,5,6,7]
# total = 0
# for n in number:
#     if n%2 == 0:
#         total +=n
# print('total :', total)

