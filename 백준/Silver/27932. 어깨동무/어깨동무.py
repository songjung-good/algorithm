n, k = map(int, input().split())
heights = list(map(int, input().split()))

def can_withstand(H):
    tired_count = 0
    i = 0
    while i < n:
        l = 0
        r = 0
        if i > 0:
            l = abs(heights[i] - heights[i-1])
        if i < n-1:
            r = abs(heights[i+1] - heights[i])
        if max(l,r) > H:
            tired_count += 1
        i += 1
    return tired_count <= k

# 이분 탐색으로 최소 H 찾기
left, right = 0, max(heights) - min(heights)
answer = right
while left <= right:
    mid = (left + right) // 2
    if can_withstand(mid):
        answer = mid
        right = mid - 1
    else:
        left = mid + 1

print(answer)