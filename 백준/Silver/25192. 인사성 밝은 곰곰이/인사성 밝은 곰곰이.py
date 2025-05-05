import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
Q = deque([])
seen = set()  # 중복 체크를 위한 set
ans = 0

for _ in range(N):
    word = input().strip()
    if word == 'ENTER':
        ans += len(Q)
        Q = deque([])  # Q 초기화
        seen = set()   # set도 초기화
    else:
        if word not in seen:  # 중복이 아니라면
            Q.append(word)
            seen.add(word)  # set에 추가

ans += len(Q)  # 마지막 그룹 처리
print(ans)