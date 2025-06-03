fibo_lst = [1, 1]
fibo_len = 2

def fibo(num):
    global fibo_len, fibo_lst
    if fibo_len >= num:
        return fibo_lst[num-1]
    else:
        for i in range(fibo_len-1, num-1):
            fibo_lst.append(fibo_lst[i-1] + fibo_lst[i])
        fibo_len = num
        return fibo_lst[num-1]

T = int(input())
for t in range(1, T+1):
    P, Q = map(int, input().split())
    ans = fibo(P) % Q
    print(f"Case #{t}: {ans}")
