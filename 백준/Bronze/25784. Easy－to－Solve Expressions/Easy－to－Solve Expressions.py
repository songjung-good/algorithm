# 코드를 작성해주세요
lst = list(map(int, input().split()))
lst.sort()
if lst[2] == lst[1] + lst[0]:
    print(1)
elif lst[2] == lst[1] * lst[0]:
    print(2)
else:
    print(3)