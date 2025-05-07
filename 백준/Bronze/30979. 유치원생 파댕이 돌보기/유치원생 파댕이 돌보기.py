T = int(input())
N = int(input())
F = list(map(int, input().split()))
for i in F:
    T -= i

if T > 0:
    print('Padaeng_i Cry')
else:
    print('Padaeng_i Happy')