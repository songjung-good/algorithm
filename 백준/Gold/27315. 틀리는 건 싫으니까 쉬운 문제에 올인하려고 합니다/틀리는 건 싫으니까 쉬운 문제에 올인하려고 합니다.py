from heapq import heappush, heappop
import sys
import math
input = sys.stdin.readline

N, M = map(int, input().split())
problem_list = list()
solvable_problem_list = list()
for _ in range(N) :
  D, P, T, E = map(int, input().split())
  _D, _P = D, P
  if T == 1 :
    P, _P = 0, 0
  if E == 1 :
    heappush(problem_list, (math.ceil(D / 2), P // 2))
  else :
    heappush(problem_list, (D, P))
HD, HP = map(int, input().split())

answer = 0
while M :
  while problem_list and HD >= problem_list[0][0] :
    D, P = heappop(problem_list)
    heappush(solvable_problem_list, P)
  if not solvable_problem_list :
    break
  P = heappop(solvable_problem_list)
  answer += max(P - HP, 0)
  HP += 1
  HD += 1
  M -= 1

print(answer if not M else -1)