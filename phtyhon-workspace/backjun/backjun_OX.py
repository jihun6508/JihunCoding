N = int(input())
a =[]
for i in range(N):
    a.append(input())
countO = 0
sum = 0
for i in range(N):
    b = a[i]
    for i in range(len(b)):
        if b[i] == "O":
            countO +=1
            sum += countO
        else:
            countO = 0
    print(sum)
    sum = 0
    countO = 0