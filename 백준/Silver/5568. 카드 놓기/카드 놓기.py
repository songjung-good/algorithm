# import sys
# input = sys.stdin.readline

def combi(num, cnt, used):
    if cnt == k:
        num = int(num)
        if num in made_num:
            pass
        else:
            made_num.append(num)
    else:
        for i in range(n):
            if used[i]:
                pass
            else:
                used[i] = 1
                new_num = num + str(n_lst[i])
                cnt += 1
                combi(new_num, cnt, used)
                cnt -= 1
                used[i] = 0

n = int(input())
k = int(input())
n_lst = [int(input()) for _ in range(n)]

made_num = []
used_num = []
for i in range(n):
    used = [0] * n
    now = n_lst[i]
    if now in used_num:
        pass
    else:
        used[i] = 1
        used_num.append(now)
        combi(str(now), 1, used)

print(len(made_num))
