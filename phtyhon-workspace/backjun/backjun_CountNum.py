A = int(input())
B = int(input())
C = int(input())
Num = str(A*B*C)
NumArray = []
for i in range(len(Num)):
    NumArray.append(Num[i])
for i in range(0,10):
    print(NumArray.count(str(i)))
