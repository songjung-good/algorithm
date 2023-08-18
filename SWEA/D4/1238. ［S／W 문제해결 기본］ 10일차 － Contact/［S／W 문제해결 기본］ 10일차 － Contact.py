T = 10
for t in range(1, T+1):
    l, s = map(int, input().split())
    lst = list(map(int, input().split()))
    dic = {}
    for i in range(l//2):
        x, y = lst[i*2], lst[i*2+1]
        if x not in dic.keys():
            dic.update({x : [y]})
        else:
            dic[x].append(y)
    last_call = dic[s]
    dic.pop(s)
    now_call = []
    v = [s]
    while True:
        for i in last_call:
            v.append(i)
            if i in dic.keys():
                for j in dic[i]:
                    if j not in v:
                        now_call.append(j)
                dic.pop(i)
        if now_call:
            last_call = now_call
            now_call = []
        else:
            break
    max_v = 0
    for k in last_call:
        if max_v < k:
            max_v = k
    print(f'#{t} {max_v}')