
from re import A


coffee = 10
money = 300
# while money:
#     print("돈을 받았으니 커피를 줍니다")
#     coffee -= 1
#     print("남은 커피의 양은 %s잔입니다." %coffee)
#     if coffee == 0:
#         print("커피가 모두 떨어졌습니다. 판매를 중단합니다.")
#         break

# while True:
#     money = int(input("돈을 넣어주세요: "))
#     if money == 300:
#         print("커피를 줍니다.")
#         coffee -= 1
#         print("남은 커피는 %d잔 입니다"%coffee)
#     elif money > 300:
#         print("거스름돈 %d원을 주고 커피를 줍니다."%(money-300))
#         coffee -= 1
#         print("남은 커피는 %d잔 입니다."%coffee) 
#     else:
#         print("돈을 다시 돌려주고 커피를 주지 않습니다.")
#         print("남은 커피는 %d잔 입니다."%coffee)
#     if coffee == 0:
#         print("커피가 떨어졌습니다. 판매를 중단합니다.")
#         break


# coffeePrice = 30
# card = int(input("충전된 카드 잔액을 입력: "))
# coffee = int(input("재고 커피양을 입력: "))

# while card and coffee:
#     if card >= coffeePrice:
#         print("커피를 줍니다.")
#         coffee -= 1
#         print("남은 커피는 %d잔 입니다"%coffee)
#         card -= coffeePrice
#         print("잔액은 %d입니다"%card)
#     else:
#         print("잔액이 부족합니다. 잔액은 %d원입니다"%card)
#         print("남은 커피는 %d잔 입니다."%coffee)
#         print("판매를 중단합니다.")
#         break
    
#     if card < 30:
#         print("잔액이 부족합니다. 잔액은 %d원입니다"%card)
#         print("판매를 중단합니다.")
#         break
    
#     if coffee == 0:
#         print("커피가 떨어졌습니다. 판매를 중단합니다.")
#         break

# while True:
#     if card >= coffeePrice and coffee > 0:
#         print("커피를 줍니다.")
#         coffee -= 1
#         print("남은 커피는 %d잔 입니다"%coffee)
#         card -= coffeePrice
#         print("잔액은 %d입니다"%card)
#         if card < coffeePrice :
#             print("잔액이 부족합니다. 잔액은 %d원입니다"%card)
#             print("판매를 중단합니다.")
#             break         
#     elif card < coffeePrice:
#         print("잔액이 부족합니다. 잔액은 %d원입니다"%card)
#         print("남은 커피는 %d잔 입니다."%coffee)
#         print("판매를 중단합니다.")
#         break
#     else:
#         print("커피가 떨어졌습니다. 판매를 중단합니다.")
#         break
#     if coffee == 0:
#         print("커피가 떨어졌습니다. 판매를 중단합니다.")
#         break        

# a = 0
# while a < 10:
#     a +=1
#     if a%2 == 0:
#         continue #바로 다음 루프로 진행
#     print(a)
#     print("컨티뉴 통과?")

a = 0
sum=0
while a < 10:
    a +=1
    if not a%2 == 0:
        continue
    else: sum +=a
print(sum)