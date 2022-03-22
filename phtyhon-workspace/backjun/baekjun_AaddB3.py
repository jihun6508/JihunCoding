# T = int(input())
# c = []
# for i in range(0,T):
#     a,b = input().split()
#     a = int(a)
#     b = int(b)
#     c.insert(i, a+b)
# for i in c:
#     print (i)

# num = int(input())
# sum = 0
# for i in range(1,num+1):
#     sum +=i
# print(sum)

# a = int(input())
# for i in range(a+1):
#     print(i)

from datetime import date


T = int(input())
c = []
e = []
f = []

for i in range(0,T):
    a,b = input().split()
    a = int(a)
    b = int(b)
    c.append(a+b)
    e.append(a)
    f.append(b)
d = 0
for i in c:
    d +=1
    print ("Case #%d: %d + %d = %d" %(d,e[d-1],f[d-1], i))