N, k = map(int, input().split())
num_lst = list(map(int, input().split()))
ans = 'Yes'
for i in range(k):
    group = num_lst[i::k]
    group.sort()
    if ans == 'No':
        break
    for idx, num in enumerate(group):
        if num != i + idx * k:
            ans = 'No'
            break

print(ans)