def solution(my_string):
    answer = ''
    for i in range(len(my_string)):
        # 이전(0 ~ i-1)까지의 문자들 중에 현재 문자(my_string[i])가 있었는지 확인
        is_duplicate = False
        for j in range(i):
            if my_string[i] == my_string[j]:
                is_duplicate = True
                break
        
        # 처음 등장한 문자라면 answer에 추가
        if not is_duplicate:
            answer += my_string[i]
            
    return answer