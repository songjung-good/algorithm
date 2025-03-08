import math
def magic(num):
    A = math.floor(num/2)
    B = math.ceil(num/2)
    return A, B

X, M = map(int,input().split())
ans = X
pix = [X]
for _ in range(M):
    new_pix = []
    for i in pix:
        A, B = magic(i)
        new_pix.append(A)
        new_pix.append(B)
    pix = new_pix
    ans += sum(new_pix)

print(ans)