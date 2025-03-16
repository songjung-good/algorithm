# 코드를 작성해주세요
T=int(input())
for t in range(T):
    N=int(input())
    school = ''
    max_num = 0
    for n in range(N):
        A, B = map(str, input().split())
        B = int(B)
        if max_num < B:
            school = A
            max_num = B
    print(school)