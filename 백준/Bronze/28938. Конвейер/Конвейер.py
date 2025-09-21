# 코드를 작성해주세요
N = int(input())
lst = list(map(int, input().split()))
num = 0
for n in range(N):
    num += lst[n]

if num == 0:
    print('Stay')
elif num > 0:
    print('Right')
else:
    print('Left')