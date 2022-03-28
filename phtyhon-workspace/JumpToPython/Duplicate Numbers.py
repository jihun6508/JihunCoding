#점프 투 파이썬 종합문제 Q15 Duplicate Numbers
def DuplicateNumber(Number):    
    CheckList = list(map(int, Number))

    CheckResult = False

    for i in range(10):
        if CheckList.count(i) !=1:
            CheckResult = False
            break
        else: CheckResult = True
    return print(CheckResult)
        
DuplicateNumber(input())