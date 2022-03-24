values = []

average = 0
sum = 0
with open("sample.txt", "r") as f1:
    for i in f1:
        sum += int(i.strip())
        values.append(int(i.strip()))
    average = sum/len(values)
        
with open("sample_result.txt", "w") as f2:
    f2.write("sum : " + str(sum) +"\naverage : " + str(average))
