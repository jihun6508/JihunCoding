prompt = """
1. Add
2. Del
3. list
4. Quit

Enter Number : """

# print(prompt)

number = 0
while number != 4:
    print(prompt)
    number = int(input("숫자 입력 : ")) #input() 임의의 키보드 입력값을 받음(Str)

