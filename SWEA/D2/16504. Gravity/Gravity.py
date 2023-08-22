'''
가로 N
세로 100
테스트케이스 T


첫 번째 줄에 테스트 케이스의 수 T가 주어진다.
각 테스트 케이스의 첫 줄에는 방의 가로길이가 주어지고
그 다음 줄부터는 쌓여있는 상자의 수가 주어진다.

떨어지는 높이는 최대 수부터 계산하여여'''

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    lst = list(map(int, input().split()))
    ans = 0

    for i in range(N):
        cnt = N - i - 1
        for j in range(i+1, N):
            if lst[i] <= lst[j]:
                cnt -= 1
        if ans < cnt:
            ans = cnt

    print(f'#{tc} {ans}')