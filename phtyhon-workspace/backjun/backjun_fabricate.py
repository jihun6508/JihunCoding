N = int(input())
A = list(map(int, input().split()))
B = sorted(A)

for i in range(len(A)):
    A[i] = (A[i]/B[N-1])*100
sum = 0
for i in A:
    sum +=i

print(sum/len(A))
