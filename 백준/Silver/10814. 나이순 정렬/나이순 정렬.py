N = int(input())
INFO = [[] for _ in range(201)]
for n in range(N):
    age, name = map(str, input().split())
    age = int(age)
    INFO[age].append(name)

for i in range(201):
    if INFO[i]:
        for j in INFO[i]:
            print(f'{i} {j}')