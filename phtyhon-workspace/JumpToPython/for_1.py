# add = 0
# for i in range(1,101):
#     add += i
# print(add)



# for i in range(2, 10):
#     for d in range(1,10):
#         print(i,"*",d,"=",i*d)
#     print()

# result = 0
# for i in range(1,1001):
#     if i%3 == 0:
#         result +=i
#     else: continue

# i = 0
# result = 0
# while i < 1000:
#     i +=1
#     if i%3 == 0 and i%5:
#         result +=i
#     else: pass
# print(result)

# i = 0
# while True:
#     i +=1
#     if i == 6 : break
#     print("*"*i)

# i = 6
# while True:
#     i -=1
#     if i == 0 : break
#     print("*"*i)
    
# i3 = int(input())
# for i in  range(0, i3):
#     print("*"*(i+1))

# t = int(input())
# for i in  range(0, t):
#     print(" "*(t-i-1) + "*"*(i+1))



a = [70, 60, 55, 75, 95, 90, 80, 85, 100, 80]
sum = 0

for i in a:
    sum += i 
avr = sum/len(a)
print(avr)