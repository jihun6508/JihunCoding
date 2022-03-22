remains = []
for i in range(0,10):
    remains.append(int(input())%42)
A = set(remains)
print(len(A))
