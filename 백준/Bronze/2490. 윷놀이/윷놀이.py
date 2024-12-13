# 코드를 작성해주세요
while True:
    try:
        num = sum(list(map(int, input().split())))
        if num == 1:
            print('C')
        elif num == 2:
            print('B')
        elif num == 3:
            print('A')
        elif num == 4:
            print('E')
        else:
            print('D')
    except:
        break