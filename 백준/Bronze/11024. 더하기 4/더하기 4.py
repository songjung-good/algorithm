# 코드를 작성해주세요
N = int(input())
for n in range(N):
    N_lst = list(map(int, input().split()))
    print(sum(N_lst))