N = int(input())
A = list(map(str, input().split()))
CNT = {}
for a in A:
    CNT[a] = 0

for n in range(N):
    name_lst = list(map(str, input().split()))
    for c in name_lst:
        CNT[c] += 1

Q = sorted(CNT.items(), key=lambda x: x[1], reverse=True)
for X in Q:
    print(X[0], X[1])