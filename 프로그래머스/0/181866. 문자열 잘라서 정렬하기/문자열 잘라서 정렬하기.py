def solution(myString):
    answer = myString.split('x')
    ans = []
    answer.sort()
    for i in range(len(answer)):
        if answer[i] == '':
            pass
        else:
            ans.append(answer[i])
            
    return ans