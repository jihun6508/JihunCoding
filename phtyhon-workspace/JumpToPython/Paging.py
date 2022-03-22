# from math import floor


# def getTotalPage(m, n):
#     return floor((m/n)+1)

# print(getTotalPage(7, 4))
import re
def hexrepl(match):
    value = int(match.group())
    return hex(value)

p = re.compile(r'\d+')
p.sub(hexrepl, 'Call 65490 for printing, 49152 for user code.')