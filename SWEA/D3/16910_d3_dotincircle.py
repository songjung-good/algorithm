'''
    반지름 N인 원 안에
    x**2 + y**2 < N**2
    x,y의 수
'''

T = int(input())


for tc in range(1, T+1):
    N = int(input())
    ans = 0

    for i in range(-N, N):
       for j in range(-N, N):
           if N**2 >= i**2 + j**2:
               ans += 1

    print(f'#{tc} {ans+2}')