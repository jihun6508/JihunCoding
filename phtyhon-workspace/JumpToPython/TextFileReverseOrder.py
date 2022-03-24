#역순저장
text = []
with open("abcd.txt", "r") as f1:
    for i in f1:
        text.append(i.strip())
text = sorted(text, reverse=True)
with open("abcd_result.txt", "w") as f2:
    for i in text:
        f2.write(i + "\n")