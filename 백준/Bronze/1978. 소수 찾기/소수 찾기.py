import math

def test(num):
    ans = True
    if num == 1:
        ans = False
    else:
        sqrt_num = math.sqrt(num)
        for i in range(2, int(sqrt_num)+1):
            if sqrt_num % i == 0:
                ans = False
                break

    return ans

def is_prime(num):
    if num == 1:
        return False
    sqrt_num = int(math.sqrt(num))
    for i in range(2, sqrt_num + 1):
        if num % i == 0:
            return False
    return True

N = int(input())
num_lst = list(map(int, input().split()))
cnt = 0
for num in num_lst:
    if is_prime(num):
        cnt += 1
print(cnt)
