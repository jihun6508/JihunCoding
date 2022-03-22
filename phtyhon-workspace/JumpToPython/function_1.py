def AloveB(a,b):
    return print(f"{a}(은)는 {b}(을)를 좋아해")
def HowMuchLove (*arg):
    LoveScore = 0
    for i in arg:   
        LoveScore += i
    return print(f"{LoveScore}만큼 사랑해")

AloveB("김지훈","김유진")
HowMuchLove(100,200,300,400,500,600,700,800)

def LoversName(**kwargs):
    return print(kwargs)

LoversName (남자친구 = "김지훈", 여자친구 = "김유진")
