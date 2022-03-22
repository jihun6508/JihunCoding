A = []
for i in range(9):
    A.append(int(input()))
B = sorted(A)
print(B[8])
print(A.index(B[8])+1)