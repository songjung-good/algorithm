import sys
input = sys.stdin.readline

def check_ice(lst, num):
    if num == len(lst):
        return True
    else:
        x, y = lst[num]
        if x in dict and dict[x] >= y:
            num += 1
            return check_ice(lst, num)
        else:
            return False


# 아이스크림 구슬 갯수 N, 아이스크림 먹는 횟수 Q
N = int(input())
COLORS = list(map(int,input().split()))
dict = {}
cnt = len(COLORS)
for c in COLORS:
    if c in dict:
        dict[c] += 1
    else:
        dict[c] = 1

Q = int(input())
for _ in range(Q):
    # 먹을 구슬 목록 A_lst, 넣을 구슬 목록 B_lst
    A_lst = list(map(int,input().split()))
    ai = A_lst.pop(0)
    if not ai:
        B_lst = list(map(int, input().split()))
        bi = B_lst.pop(0)
        for b in B_lst:
            if b in dict:
                dict[b] += 1
            else:
                dict[b] = 1
    else:
        ai_lst = []
        check = A_lst[0]
        check_cnt = 1
        for i in range(1, ai):
            if A_lst[i] != check:
                ai_lst.append((check, check_cnt))
                check = A_lst[i]
                check_cnt = 1
            else:
                check_cnt += 1
        ai_lst.append((check, check_cnt))

        if check_ice(ai_lst, 0):
            for x, y in ai_lst:
                dict[x] -= y
            B_lst = list(map(int, input().split()))
            bi = B_lst.pop(0)
            for b in B_lst:
                if b in dict:
                    dict[b] += 1
                else:
                    dict[b] = 1
        else:
            B_lst = list(map(int,input().split()))

ans = []
ans_num = 0
for i in dict:
    ans_num += dict[i]
    for _ in range(dict[i]):
        ans.append(i)
print(ans_num)
print(*ans)