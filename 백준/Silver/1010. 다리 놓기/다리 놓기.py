def fact(num):
    number = 1
    for n in range(1, num+1):
        number *= n

    return number

T = int(input())
for t in range(T):
    N, M = map(int, input().split())

    ans = fact(M) // (fact(N) * fact(M-N))
    print(ans)