import sys
input = sys.stdin.readline

N = int(input())
A_lst = list(map(int, input().split()))
togle = [1] * (N+1)
handle = [0] * (N+1)
cnt = sum(A_lst)
print(cnt)

Q = int(input())
for _ in range(Q):
    Q_lst = list(map(int, input().split()))
    node = Q_lst[1]
    if Q_lst[0] == 1:
        if togle[node]:
            if handle[node]:
                cnt -= handle[node]
            else:
                cnt -= A_lst[node-1]
            handle[node] = Q_lst[2]
            cnt += handle[node]
        else:
            handle[node] = Q_lst[2]
    else:
        if togle[node]:
            if handle[node]:
                cnt -= handle[node]
            else:
                cnt -= A_lst[node-1]
            togle[node] = 0
        else:
            togle[node] = 1
            if handle[node]:
                cnt += handle[node]
            else:
                cnt += A_lst[node-1]
    print(cnt)