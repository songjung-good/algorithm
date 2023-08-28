T = int(input())
for tc in range(1, 1+T):
    #전체 N, 제출자 A
    N, A = map(int, input().split())
    A_lst = list(map(int, input().split()))
    student = [i+1 for i in range(N)]
    for i in A_lst:
        if i in student:
            student.remove(i)

    print(f'#{tc}', end=" ")
    print(*student)