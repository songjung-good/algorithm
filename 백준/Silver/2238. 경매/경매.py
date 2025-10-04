U, N = map(int, input().split())
dic = {}
for _ in range(N):
    S, P = map(str, input().split())
    P = int(P)
    if P in dic:
        dic[P].append(S)
    else:
        dic[P] = [S]

dic2 = {}
lst = sorted(dic.keys())
for i in lst:
    num = len(dic[i])
    if num in dic2:
        pass
    else:
        dic2[num] = [dic[i][0], i]

lst = sorted(dic2.keys())
print(dic2[lst[0]][0], dic2[lst[0]][1])