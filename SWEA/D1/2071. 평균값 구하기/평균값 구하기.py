T = int(input())
for tc in range(1, T+1):
    num_lst = list(map(int, input().split()))
    ans = sum(num_lst)
    print(f'#{tc} {round(ans/10)}')