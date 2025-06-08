N, L = map(int, input().split())
fruits = list(map(int, input().split()))
fruits.sort()

for n in range(N):
    if fruits[n] <= L:
        L += 1
    else:
        break

print(L)