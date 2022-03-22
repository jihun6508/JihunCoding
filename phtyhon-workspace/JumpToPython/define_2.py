# def profileInput(name, age, address):
#     print(f"제 이름은 {name}이고 나이는 {age}이고 사는 곳은 {address}입니다")

# profileInput(
#     input("이름을 입력하세요>> "),
#     input("나이를 입력하세요>> "),
#     input("주소를 입력하세요>> ")
# )

# def add_many(*args):
#     result = 0
#     for i in args:
#         result +=i
#     return result

# result = add_many(1,2,3,4,5)

# print(result)

def add_mul(choice, *args):
    if choice == "add":
        result = 0
        for i in args:
            result +=i
    elif choice == "mul":
        result = 1
        for i in args:
            result *=i
    return result

result = add_mul ('add', 1,2,3,4,5,6)
print(result)

result = add_mul('mul', 1,2,3,4,5,6)
print(result)