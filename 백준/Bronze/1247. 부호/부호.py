# 코드를 작성해주세요
while True:
    try:
        A=int(input())
        num = 0
        for a in range(A):
            n = int(input())
            num += n
        if num == 0:
            print(0)
        elif num > 0:
            print('+')
        else:
            print('-')
    except:
        break