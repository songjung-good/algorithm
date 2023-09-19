def fac(num):
    ans = 1
    for i in range(1, num+1):
       ans *= i
    return ans


A=int(input())
print(fac(A))
