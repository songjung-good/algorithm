def solution(n):
    answer = 0
    cnt = 1
    for _ in range(n):
        while True:
            if cnt % 3 and '3' not in str(cnt):
                cnt += 1
                break
            else:
                cnt += 1
        

    return cnt-1