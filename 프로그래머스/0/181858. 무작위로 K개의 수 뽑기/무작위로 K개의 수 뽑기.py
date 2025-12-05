def solution(arr, k):
    answer = []
    cnt = 0
    for i in arr:
        if not i in answer:
            answer.append(i)
            cnt += 1
        if cnt == k:
            break
        
    N = k - len(answer)
    if N:
        for _ in range(N):
            answer.append(-1)

    return answer