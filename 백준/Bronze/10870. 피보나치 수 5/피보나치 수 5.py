def fibo(num):
    if num == 1:
        return 0
    elif num == 2:
        return 1
    else:
        ans = fibo(num - 1) + fibo(num - 2)
        return ans


A=int(input())
# ans = 0
# for i in range(1, A+1):
#     ans += fibo(i)

print(fibo(A+1))