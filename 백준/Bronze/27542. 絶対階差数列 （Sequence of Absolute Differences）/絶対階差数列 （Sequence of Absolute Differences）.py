N = int(input())
N_lst = list(map(int, input().split()))

while N > 2:
    N = N - 1
    lst = []
    for i in range(N):
        lst.append(abs(N_lst[i] - N_lst[i+1]))
    N_lst = lst

print(abs(N_lst[0]-N_lst[1]))
