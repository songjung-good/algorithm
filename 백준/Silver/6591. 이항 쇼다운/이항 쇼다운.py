while True:
    n, k = map(int,input().split())
    A = 1
    B = 1
    if n == 0 and k == 0:
        break

    num = min(n-k, k)
    for i in range(num):
        A *= n-i
        B *= (i+1)

    print(A//B)