# 가로 크기 W, 세로 크기 H, 접는 점 f, c + 1개로 같은 크기
W, H, f, c, x1, y1, x2, y2 = map(int, input().split())

# 겹쳐지는 부분 찾기
a = min(W - f, f)
b = max(W - f, f)
# 0 ~ a까지 a ~  b
ans = 0
if x1 <= a:
    if x2 <= a:
        ans += (x2 - x1) * 2
    else:
        ans += (a - x1) * 2 + (x2 - a)
else:
    ans += x2 - x1
ans *= (y2 - y1)
print(W * H - ans * (c + 1))