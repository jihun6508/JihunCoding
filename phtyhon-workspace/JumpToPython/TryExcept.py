result = 0

try:
    4/1
    [1, 2, 3][3]
    3+1
    4 / 0
except IndexError:
    pass
except TypeError:
    result += 1
except ZeroDivisionError:
    result += 2
finally:
    result += 4

print(result)