T = int(input())
a_reward = [0, 500, 300, 200, 50, 30, 10]
a_rank = [0, 1, 2, 3, 4, 5, 6]
b_reward = [0, 512, 256, 128, 64, 32]
b_rank = [0, 1, 2, 4, 8, 16]
for _ in range(T):
    ans = 0
    a, b = map(int, input().split())
    for i in range(7):
        if a <= 0:
            ans += a_reward[i]
            break
        else:
            if i == 6:
                break
            else:
                a -= a_rank[i+1]

    for i in range(6):
        if b <= 0:
            ans += b_reward[i]
            break
        else:
            if i == 5:
                break
            else:
                b -= b_rank[i+1]
    print(ans * 10000)
