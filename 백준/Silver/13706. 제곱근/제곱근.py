A = int(input())
start = 0
end = A

while True:
    mid = (start + end) // 2
    num = mid ** 2
    if num == A:
        print(mid)
        break
    elif num > A:
        end = mid
    elif num < A:
        start = mid
