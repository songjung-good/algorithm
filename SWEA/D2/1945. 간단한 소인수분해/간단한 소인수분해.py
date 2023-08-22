'''
N=2a x 3b x 5c x 7d x 11e

N이 주어질 때 a, b, c, d, e

가장 첫 줄에는 테스트 케이스의 개수 T가 주어지고, 그 아래로 각 테스트 케이스가 주어진다.

각 테스트 케이스의 첫 번째 줄에 N 이 주어진다.
'''

def made_ans(N):
    a, b, c, d, e = 0, 0, 0, 0, 0
    while N % 2 == 0:
        N = N/2
        a += 1
    while N % 3 == 0:
        N = N / 3
        b += 1
    while N % 5 == 0:
        N = N / 5
        c += 1
    while N % 7 == 0:
        N = N / 7
        d += 1
    while N % 11 == 0:
        N = N / 2
        e += 1

    return [a, b, c, d, e]


T = int(input())
for tc in range(1, T+1):
    lst = made_ans(int(input()))
    print(f'#{tc} {" ".join(map(str, lst))}')
