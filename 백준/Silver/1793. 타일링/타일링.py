DP = [1] * 251
DP[2] = 3 
now = 2
while True:
    try:
        n = int(input())
        if n > now:
            for i in range(now, n+1):
                DP[i] = DP[i-1] + (DP[i-2] * 2)
            now = n
        print(DP[n])
    except:
        break
