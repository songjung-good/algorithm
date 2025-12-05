def solution(arr, n):
    answer = []
    num = len(arr)
    if num % 2:
        for i in range((num+1) // 2):
            arr[i*2] += n
    else:
        for i in range(num // 2):
            arr[i*2 + 1] += n
    return arr