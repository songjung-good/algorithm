# 코드를 작성해주세요
N = int(input())
lst = [int(input()) for _ in range(N)]
num = lst[0]
if max(lst) == num:
    print('hard')
elif min(lst) == num:
    print('ez')
else:
    print('?')