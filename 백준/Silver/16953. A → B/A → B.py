# 코드를 작성해주세요
def find_ans(num):
    cnt = 1
    while A < num:
        if num % 10 == 1:
            num //= 10
        elif num % 2 == 0:
            num //= 2
        else:
            break
        cnt += 1

    if num == A:
        return cnt
    else:
        return -1


A, B = map(int, input().split())
print(find_ans(B))
