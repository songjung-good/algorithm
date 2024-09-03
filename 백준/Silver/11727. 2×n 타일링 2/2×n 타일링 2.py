'''
1. 사용되는 블럭의 수가 아닌 채울 수 있는 방법의 수
2. 타일을 채우는 블럭의 종류는 3가지
3. 가로 0칸이면 방법 0
    가로 1칸이면 방법 1 (1x2)
    가로 2칸이면 방법 3 (1x2 * 2, 2x1 * 2, 2x2)
4. 해당 과정을 점화식으로 진행
'''

'''
방법 1. 함수를 이용
def dp(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 3
    else:
        return dp(n-1) + (2 * dp(n-2))
    
# 입력값 받기
N = int(input())
# 함수 진행
print(dp(N))
'''

# 방법 2 반복문 활용
N = int(input())
dp = [0] * 1001
dp[1] = 1
dp[2] = 3

if N <= 2:
    pass
else:
    for n in range(3, N+1):
        dp[n] = dp[n-1] + 2*dp[n-2]

print(dp[N] % 10007)