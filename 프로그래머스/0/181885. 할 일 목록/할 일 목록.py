def solution(todo_list, finished):
    answer = []
    zipped = list(zip(finished, todo_list))
    for a, b in zipped:
        if a:
            pass
        else:
            answer.append(b)
    return answer