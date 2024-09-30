import sys
input = sys.stdin.readline

N = int(input())
SCORE = []
CHECK = [100, 100, 100, 100, 100, 100, 100]

for n in range(N):
    SCORE.append(float(input()))

A = 100
for i in SCORE:
    if i >= A:
        pass
    else:
        CHECK.remove(A)
        CHECK.append(i)
        A = max(CHECK)

CHECK.sort()
for j in CHECK:
    print(format(j, '.3f'))
