N = int(input())
A = []
sum = 0
overAvr = 0.0
resultlist = []
for i in range(N):
    A = list(map(int, input().split()))
    p = 0
    for t in A:
        p +=1
        if p == 1:
            continue
        sum +=t
    p = 0
    for z in A:
        p += 1 #p=2
        # if z == A[0] 8:
        #     continue
        if p == 1:
            continue
        if sum/A[0] < z:
            overAvr +=1
    result = round(overAvr/A[0]*100,3)
    resultlist.append('%0.3f'%result+"%")
    overAvr = 0
    sum = 0
for i in resultlist:
    print(i)


