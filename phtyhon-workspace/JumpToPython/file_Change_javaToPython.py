
import randomPop

a = randomPop.random_pop()

with open("test.txt", 'r') as f1:
    data = f1.read()

data = data.replace("java","python")
print(data)
with open("test.txt", 'w') as f1:
    f1.write(data)
