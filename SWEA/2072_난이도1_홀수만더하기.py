```
dadadafagaga
```
N = int(input())
X = int(1)


for i in range(N):
    A = list(map(int, input().split()))
    B = int(0)
    for j in A:
        if j % 2 == 1:
            B += j
        elif j % 2 == 0:
            B = B
    print("%s%s %d" %("#", X, B))
    X += 1
