N = int(input())

for n in range(N):
    A = int(input())
    B = (A // 2) + 1
    ans = []
    for i in range(1, B+1):
        for j in range(i+1, A):
            num = i + j
            if num == A:
                ans.append(str(i) + ' ' + str(j))

    print(f"Pairs for {A}: {', '.join(ans)}")