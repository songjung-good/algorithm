def solution(n_str):
    answer = ''
    cnt = 0
    while True:
        if n_str[cnt] != '0':
            break
        cnt += 1
    return n_str[cnt:]