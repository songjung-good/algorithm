C = int(input())
for c in range(C):
    # n_lst 학생점수, N 학생수, M 평균넘는 수, AVG 평균값,
    n_lst = list(map(int, input().split()))
    N = n_lst.pop(0)
    M = 0
    AVG = float(sum(n_lst) / N)
    for i in n_lst:
        if i > AVG:
            M += 1
    ans = float((M / N)*100)
    print(f'{ans:.3f}%')