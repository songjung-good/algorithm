A, B = map(int, input().split())
A_lst = list(map(int, input().split()))
B_lst = list(map(int, input().split()))

ans = sum(A_lst) + sum(B_lst)
print(ans)