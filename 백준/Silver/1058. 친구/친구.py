N = int(input())
F = {}
for n in range(N):
    F[n] = []
    now = input()
    for i in range(N):
        if now[i] == 'Y':
            F[n].append(i)

max_cnt = 0
for x in range(N):
    now = 0
    for y in range(N):
        if x == y:
            pass
        else:
            if y in F[x]:
                now += 1
            else:
                for z in F[x]:
                    if y in F[z]:
                        now += 1
                        break
                    else:
                        pass
    if now > max_cnt:
        max_cnt = now

print(max_cnt)
