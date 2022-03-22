n, X = map(int, input().split())
A = [] #n개짜리 리스트
A = list(map(int, input().split()))

for i in A:
    if i < X:
        print(i, end=" ")