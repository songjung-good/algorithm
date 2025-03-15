'''
각 게시글의 정보
1. 게시글 번호
2. 게시글 랭킹
3. 게시글의 키워드 수
4. 게시글의 키워드
키워드가 포함된 게시글의 번호를 랭킹의 순서대로 출력
'''
import copy

N, M = map(int, input().split())
rank = list(map(int, input().split()))
new_rank = []
for n in range(1, N+1):
    new_rank.append(rank.index(n) + 1)
    
board = [[]]
for n in range(1, N+1):
    lst = list(map(int, input().split()))
    board.append(lst[1:])

Q = int(input())
for _ in range(Q):
    k = int(input())
    ans = copy.deepcopy(new_rank)
    for n in range(1, N+1):
        if k not in board[n]:
           ans.remove(n)
    if ans:
        print(*ans)
    else:
        print(-1)
