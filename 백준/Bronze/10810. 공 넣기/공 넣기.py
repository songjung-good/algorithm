'''
바구니 N개
공 넣는 시간 M번
1~N번 바구니에 들어있는 공 번호 출력
'''

N, M = map(int, input().split())
# 1번부터 N번 바구니
basket = [0] * (N)
for _ in range(M):
    i, j, k = map(int, input().split())
    for ball in range(i-1, j):
        basket[ball] = k

print(*basket)