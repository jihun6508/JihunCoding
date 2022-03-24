#점프 투 파이썬 종합문제 14. DashInsert 문제
from copy import deepcopy


def DashInsert(a):
    alist = list(map(int, str(a)))
    postNum = ""
    resultList = []
    resultList = deepcopy(alist)
    idx = 0
    for valStr in alist:
        val = int(valStr)
        if postNum == "짝수" and val%2 == 0:
            resultList.insert(idx, "*")
            idx +=1
        else: pass
        if postNum == "홀수" and val%2 == 1:
            resultList.insert(idx, "-")
            idx+=1
        else: pass
        if val%2 == 0:
            postNum = "짝수"
        elif val%2 == 1 :
            postNum = "홀수"
        else : postNum = ""
        idx +=1
    result = ''.join(map(str, resultList))
    return print(result)
DashInsert(4546793)


