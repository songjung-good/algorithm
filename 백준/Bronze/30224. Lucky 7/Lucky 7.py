# 코드를 작성해주세요
word = input()
num = int(word)

if num % 7:
    if '7' in word:
        print(2)
    else:
        print(0)
else:
    if '7' in word:
        print(3)
    else:
        print(1)