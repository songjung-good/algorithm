#1개, 퀸 1개, 룩 2개, 비숍 2개, 나이트 2개, 폰 8개
K, Q, L, B, N, P = map(int, input().split())

a = 1 - K
b = 1 - Q
c = 2 - L
d = 2 - B
e = 2 - N
f = 8 - P

print(f'{a} {b} {c} {d} {e} {f}')