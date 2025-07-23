def solution(participant, completion):
    answer = ''
    participant.sort()
    completion.sort()
    A = len(completion)
    
    for a in range(A):
        if participant[a] == completion[a]:
            pass
        else:
            answer = participant[a]
            break
    if answer == '':
        answer = participant[A]
    return answer