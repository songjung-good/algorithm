def solution(phone_number):
    cnt = len(phone_number)
    answer = '*' * (cnt-4)
    answer += str(phone_number[cnt-4:])
    
    return answer