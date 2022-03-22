A = 1
B = 1
while A != 0 and B != 0:
    A,B = map(int, input().split())
    if A ==0 and B == 0:
        break
    print(A + B)
    
A = 0
B = 0
while True:
    try:
        A,B = map(int, input().split())
        print(A + B)
    except EOFError:
        break
