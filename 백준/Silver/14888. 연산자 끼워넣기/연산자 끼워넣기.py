'''
시작수 정하기
연산자 뽑기
다음수 뽑기
'''
def find_num(n, cnt):
    global max_num, min_num
    if n == N:
        if max_num < cnt:
            max_num = cnt
        if min_num > cnt:
            min_num = cnt
        return 
    now = n_lst[n]
    for i in range(4):
        if a_lst[i] == 0:
            pass
        else:
            n_cnt = 0
            if i == 0:
                n_cnt = cnt + now
            elif i == 1:
                n_cnt = cnt - now
            elif i == 2:
                n_cnt = cnt * now
            elif i == 3:
                if cnt < 0:
                    n_cnt = abs(cnt) // now * -1
                else:
                    n_cnt = cnt // now
            a_lst[i] -= 1
            find_num(n+1, n_cnt)
            a_lst[i] += 1
    return
                
N = int(input())
n_lst = list(map(int, input().split()))
a_lst = list(map(int, input().split()))
max_num, min_num = float('-inf'), float('inf')
find_num(1, n_lst[0])
print(max_num)
print(min_num)
