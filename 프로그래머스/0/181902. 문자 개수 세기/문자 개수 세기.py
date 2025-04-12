def solution(my_string):
    answer = [0] * 52
    for m in my_string:
        now = ord(m)
        # 65 ='A', 97 = 'a'
        if now > 96:
            answer[now-71] += 1
        else:
            answer[now-65] += 1
    return answer