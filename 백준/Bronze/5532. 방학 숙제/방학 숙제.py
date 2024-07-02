L = int(input())
A = int(input())
B = int(input())
C = int(input())
D = int(input())

X = A // C
if A % C > 0:
    X += 1

Y = B // D
if B % D > 0:
    Y += 1

Z = max(X, Y)

ans = L - Z
print(ans)