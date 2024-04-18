def tri(lst):
    lst.sort()
    ans = "Invalid"
    if lst[0] == 0:
        pass
    elif lst[0] + lst[1] <= lst[2]:
        pass
    else:
        if lst[0] == lst[1] == lst[2]:
            ans = "Equilateral"
        elif lst[1] == lst[0] or lst[1] == lst[2]:
            ans = "Isosceles"
        else:
            ans = 'Scalene'
    return ans

while True:
    lst = list(map(int, input().split()))
    if sum(lst) == 0:
        break
    else:
        print(tri(lst))