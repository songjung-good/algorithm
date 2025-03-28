from collections import deque
N = int(input())
Q = deque([])
for _ in range(N):
    char, num = input().split()
    Q.append((char, num))

# print(Q)

while len(Q) > 1:
    now_c, now_n = Q.popleft()
    Q.rotate(1-int(now_n))
    Q.popleft()

c, n = Q.popleft()
print(c)
