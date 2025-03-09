from bisect import bisect_left

N = int(input())
N_lst = list(map(int, input().split()))
dp = []

for num in N_lst:
    idx = bisect_left(dp, num)  # num이 들어갈 위치 찾기
    if idx == len(dp):
        dp.append(num)  # 가장 큰 값이면 추가
    else:
        dp[idx] = num  # 적절한 위치에 갱신 (길이는 유지)

print(len(dp))
