def solution(my_string):
    arr=[]
    for s in my_string:
        arr.append(s.lower())
    arr.sort()
    answer= ''.join(arr)
    return answer