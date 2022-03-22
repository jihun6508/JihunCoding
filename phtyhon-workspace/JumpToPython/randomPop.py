import random
def random_pop(data):
    number = random.randint(0, len(data)-1)  #len(data) = 5-1  // randit(1, 5)
    return data.pop(number)


if __name__ == "__main__":
    data = [1, 2, 3, 4, 5] # data[5] =error  #data[4] 
    while data :
        print(random_pop(data))