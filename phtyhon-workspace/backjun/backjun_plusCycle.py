import math
N = int(input())
Cyclecount = 0
result = N
while True:
    if result < 10:
        result10 =0
    else:
        result10 = math.floor(result/10)
    result1 = result%10
    resultLast = result1 + result10
    result = result1 * 10 + resultLast%10
    Cyclecount +=1
    if result == N:
        break
print(Cyclecount)

    