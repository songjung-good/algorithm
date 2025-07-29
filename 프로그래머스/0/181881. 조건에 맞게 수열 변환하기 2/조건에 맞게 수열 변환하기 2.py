def solution(arr):
    answer = 0
    num = len(arr)
    while True:
        lst = []
        answer += 1
        check = True
        for n in range(num):
            now = arr[n]
            if now >= 50 and now % 2 == 0:
                lst.append(now//2)
            elif now < 50 and now % 2:
                lst.append(now*2+1)
            else:
                lst.append(now)
            if lst[n] != arr[n]:
                check = False
            
        if check:
            break
        else:
            arr = lst

    return answer-1