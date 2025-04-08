N = int(input())
dict = {}
for n in range(N):
    x, y = map(int, input().split())
    if y in dict:
        dict[y].append(x)
    else:
        dict[y] = [x]

Y=list(dict)
Y.sort()

for y in Y:
    dict[y].sort()
    for x in dict[y]:
        print(x, y)