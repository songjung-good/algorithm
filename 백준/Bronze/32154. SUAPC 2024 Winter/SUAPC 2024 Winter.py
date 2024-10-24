# 코드를 작성해주세요
A = 'A'
B = 'B'
C = 'C'
D= 'D'
E = 'E'
F = 'F'
G= 'G'
H ='H'
I = 'I'
J = 'J'
K = 'K'
L = 'L'
M = 'M'
ans = [
    [],
    [A, B, C, D, E, F, G, H, J, L, M],
    [A, C, E, F, G, H, I, L, M],
    [A, C, E, F, G, H, I, L, M],
    [A, B, C, E, F, G, H, L, M],
    [A, C, E, F, G, H, L, M],
    [A, C, E, F, G, H, L, M],
    [A, C, E, F, G, H, L, M],
    [A, C, E, F, G, H, L, M],
    [A, C, E, F, G, H, L, M],
    [A, B, C, F, G, H, L, M],
]

word = int(input())

cnt = ans[word]
print(len(cnt))
print(*cnt)