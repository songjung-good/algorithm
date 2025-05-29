# 코드를 작성해주세요
N = int(input())
CUPS = [0] * 4
CUPS[1] = 1
for _ in range(N):
    A, B = map(int, input().split())
    CUPS[A], CUPS[B] = CUPS[B], CUPS[A]

for i in range(4):
    if CUPS[i]:
        print(i)
        exit()