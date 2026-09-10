def solution(numbers):
    answer = []
    numbers.sort()

    cnt = len(numbers)
    for i in range(cnt-1):
        for j in range(i+1, cnt):
            now = numbers[i]+numbers[j]
            if now in answer:
                pass
            else:
                answer.append(now)
    answer.sort()
    return answer