T = int(input())
for t in range(T):
    print(f'Scenario #{t+1}:')
    m = int(input())
    word = []
    for _ in range(m):
        word.append(input())
    n = int(input())
    for _ in range(n):
        ans = ''
        n_lst = list(map(int, input().split()))
        for i in n_lst[1:]:
            ans += word[i]
        print(ans)
    print()