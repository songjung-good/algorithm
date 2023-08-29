def dfs(v):
    if len(s) == M:
        print(*s)
        return

    used = {}  # 중복 검사용 딕셔너리
    for i in range(N): # {dic}.get(key, default) 키가 있으면 벨류값을 반환, 없으면 디폴트를 벨류로 하는 새 딕셔너리 추가
        if i not in v and used.get(lst[i], 0) == 0:
            used[lst[i]] = 1
            s.append(lst[i])
            new_v = v + [i]
            dfs(new_v)
            s.pop()


N, M = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()
s = []
v = []
dfs(v)