A, B = map(int,input().split())
N = int(input())
N_lst = [A]
min_gap = 1001
btn = 0
for _ in range(N):
    N_lst.append(int(input()))

for n in N_lst:
    now = abs(B-n)
    if now < min_gap:
        min_gap = now
        btn = n

if A == btn:
    print(min_gap)
else:
    print(min_gap+1)
