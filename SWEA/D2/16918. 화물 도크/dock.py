T = int(input())
for tc in range(1, T+1):
    N = int(input())
    time_table = []
    for _ in range(N):
        st, et = map(int, input().split())
        time_table.append([st, et])

    time_table.sort(key=lambda x: x[1])

    ans = 1
    past_et = time_table[0][1]

    for time in range(len(time_table)):
        if past_et <= time_table[time][0]:
            past_et = time_table[time][1]
            ans += 1

    print(f'#{tc} {ans}')