N = int(input())
check_lst = list(input().split())
lst = list(input().split())

for c in check_lst:
    if c not in lst:
        print(c)
        break