N, L = map(int, input().split())
max_num = 0
cnt = 0

for _ in range(N):
    line = input()
    line_cnt = 0
    past = '0'
    for l in range(L):
        if line[l] == '1':
            if past == '0':
                past = '1'
                line_cnt += 1
        else:
            if past == '1':
                past = '0'

    if max_num == line_cnt:
        cnt += 1
    elif max_num < line_cnt:
        cnt = 1
        max_num = line_cnt

print(max_num, cnt)
