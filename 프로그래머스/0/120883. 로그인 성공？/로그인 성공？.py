def solution(id_pw, db):
    answer = ''
    for data in db:
        if data == id_pw:
            answer = 'login'
            break
        else:
            if data[0] == id_pw[0]:
                answer = 'wrong pw'
            else:
                if answer == '':
                    answer = 'fail'
    return answer