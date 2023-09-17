'''
1 ~ 30번 학생
28명 제출 (각 줄 마다 있음)
제출 안한 번호 출력
'''
num_lst = []
for _ in range(10):
    div_num = int(input())
    A = div_num % 42
    if A not in num_lst:
        num_lst.append(A)

print(len(num_lst))