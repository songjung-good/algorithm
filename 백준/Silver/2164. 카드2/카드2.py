N = int(input())
lst = list(range(1, N+1))
new = []
while len(lst) != 1:
    length = len(lst)
    mid = length // 2
    if length % 2 == 0:
        for i in range(mid):
            new.append(lst[i*2+1])
        lst = new
        new = []
    else:
        new.append(0)
        for i in range(mid):
            new.append(lst[i*2+1])
        lst = new
        new = []
print(*lst)