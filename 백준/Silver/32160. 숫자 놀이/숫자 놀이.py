from collections import deque

N = int(input())
if N % 2:
    if (N-1) % 4:
        print(N-1)
    else:
        print(N)
else:
    if N % 4:
        print(N - 1)
    else:
        print(N)

Q = deque(range(N, 0, -1))
# Q.rotate(-1)와 같음
Q.append(Q.popleft())

while len(Q) > 2:
    a = Q.popleft()
    b = Q.popleft()
    diff = abs(a-b)
    print(a, b, sep=' ')
    temp = Q.pop()  # 오른쪽 회전 효과
    Q.append(diff)
    Q.append(temp)  # 왼쪽 회전 효과

print(Q[1], Q[0], sep=' ')