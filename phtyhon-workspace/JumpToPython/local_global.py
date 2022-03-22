def circle_area():
    area = 3.14 * radius**2
    return area

def circle_area():
    global area
    area = 3.14* radius ** 2
    return area

area = "이진수"
radius = float(input("반지름을 입력하세요>> "))
print(area)



area = 0

radius = float(input("반지름을 입력하세요>> "))
print("원의 넓이: ", circle_area())
print(area)