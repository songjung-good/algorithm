'''
바구니 N개
공 바꾸는 횟수 M번
1~N번 바구니에 들어있는 공 번호 출력
'''

N, M = map(int, input().split())
# 1번부터 N번 바구니
basket = [i+1 for i in range(N)]
for _ in range(M):
    i, j = map(int, input().split())
    basket[j-1], basket[i-1] = basket[i-1], basket[j-1]

print(*basket)