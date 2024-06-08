N = int(input())
ans = []
cnt = 0
for i in range(N):
    File = input()
    # 첫 번째 파일이면
    if i == 0:
        for i in File:
            ans.append(i)
        cnt = len(ans)
    # 첫 파일이 아니면
    else:
        for j in range(cnt):
            if ans[j] == File[j]:
                pass
            else:
                ans[j] = '?'

ans = "".join(ans)
print(ans)