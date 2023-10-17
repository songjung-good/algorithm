t=int(input())
dp=[0]*20
dp[0]=0
dp[1]=1
dp[2]=2
dp[3]=4
dp[4]=7
for i in range(5,15):
    dp[i]=dp[i-1]+dp[i-2]+dp[i-3]

for i in range(t):
    n=int(input())
    print(dp[n])
    