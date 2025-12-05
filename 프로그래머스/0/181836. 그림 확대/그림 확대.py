def solution(picture, k):
    answer = []
    for i in picture:
        save = ''
        for j in i:
            save += j * k
        for _ in range(k):
            answer.append(save)
    return answer