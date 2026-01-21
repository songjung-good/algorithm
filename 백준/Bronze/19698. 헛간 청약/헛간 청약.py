# 코드를 작성해주세요
N, W, H, L = map(int, input().split())
ans = (W // L) * (H // L)
if ans > N:
    print(N)
else:
    print(ans)