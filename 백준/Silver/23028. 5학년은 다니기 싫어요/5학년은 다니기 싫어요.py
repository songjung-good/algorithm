import sys
input = sys.stdin.readline

# 수강 학기 N, 수강 전공 A, 수강 학점 B
N, A, B = map(int, input().split())
SJT = [list(map(int, input().split())) for _ in range(10)]

for n in range(8-N):
    A_sjt = SJT[n][0]
    B_sjt = SJT[n][1]
    if A_sjt + B_sjt > 6:
        B_sjt = 6 - A_sjt

    A += A_sjt * 3
    B += (B_sjt+A_sjt) * 3

if A >= 66 and B >= 130:
    print('Nice')
else:
    print('Nae ga wae')
