# 코드를 작성해주세요
N, k = map(int, input().split())
n_lst = sorted(list(map(int, input().split())), reverse=True)

print(n_lst[k-1])