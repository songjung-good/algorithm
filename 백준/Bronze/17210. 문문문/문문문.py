# 코드를 작성해주세요
N = int(input())
S = int(input())
if N >= 6:
    print('Love is open door')
else:
    for n in range(1, N):
        if S == 0:
            print(1)
            S = 1
        else:
            print(0)
            S = 0