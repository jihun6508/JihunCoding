def is_odd (a) :
    if a%2 == 1:
        return print("훌수입니다")
    else: return print("짝수입니다")
    
is_odd(1)
is_odd(2)

def average(*args):
    result = sum(args[1:])/len(args)
    return print(result)

average(1,2,5,4,6,8)