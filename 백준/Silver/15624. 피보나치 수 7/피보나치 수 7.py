N = int(input())
fibo_lst = [0, 1, 1]

if N <= 2:
    num2 = fibo_lst[N]
else:
    for n in range(3, N+1):
        fibo_num = (fibo_lst[n-1] + fibo_lst[n-2])%1000000007
        fibo_lst.append(fibo_num)
    num2 = fibo_lst[N]

print(num2)
