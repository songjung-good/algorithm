word=input()
num=len(word)
now=0
while True:
    A = now*10
    B = 10*(now+1)
    if num > A:
        print(word[A:B])
    else:
        print(word[A:])
        break
    now+=1