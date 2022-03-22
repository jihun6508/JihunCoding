import sys

T = int(input())
c = []
for i in range(0,T):
    a,b = sys.stdin.readline().split()
    a = int(a)
    b = int(b)
    c.insert(i, a+b)
for i in c:
    print (i)
