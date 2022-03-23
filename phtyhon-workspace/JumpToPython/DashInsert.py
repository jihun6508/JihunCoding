def DashInsert(a):
    alist = list(map(int, str(a)))
    postNum = ""
    resultList = alist
    for idx, val in list(enumerate(alist)):  #idx: 0123456 val: 4546793 
        if postNum == "짝수" and val%2 == 0:
            resultList.insert(idx, "*")
        else: pass
        if postNum == "홀수" and val%2 == 1:
            resultList.insert(idx, "-")
        else: pass
        if val%2 == 0:
            postNum = "짝수"
        elif val%2 == 1 :
            postNum = "홀수"
        else : postNum = ""
    result = ''.join(map(str, resultList))
    return print(result)
DashInsert(4546793)
        
        