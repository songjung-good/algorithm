'''
바구니 N개
M회 바구니 순서 바꾸기

'''

N, M = map(int, input().split())
basket = [k for k in range(0, N+1)]

for _ in range(M):
    i, j = map(int, input().split())
    
    basket[i:j+1] = basket[j:i-1:-1]

ans = basket[1:]
print(*ans)
