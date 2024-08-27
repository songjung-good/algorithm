fibo_lst = [0, 1]

for i in range(40):
    fibo_lst.append(fibo_lst[-1] + fibo_lst[-2])

T = int(input())
for t in range(T):
    N = int(input())
    if N == 0:
        print(1, 0)
    elif N == 1:
        print(0, 1)
    else:
        print(fibo_lst[N-1], fibo_lst[N])
