A, B = map(int, input().split())
ans = []
B = B % 10

for i in range(1, A+1):
    j = i
    if i >= 10:
        j = j % 10
    if j == B or j == (2*B):
        pass
    else:
        ans.append(i)
print(len(ans))
print(*ans)