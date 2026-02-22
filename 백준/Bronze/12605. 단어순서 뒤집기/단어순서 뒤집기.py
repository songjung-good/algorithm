N = int(input())

for n in range(1, N+1):
    ans = ''
    lst=list(input().split())
    for i in range(len(lst)):
        ans += lst[-1-i]
        if i + 1 != len(lst):
            ans += ' '

    print(f'Case #{n}: {ans}')