H, M, S = map(int, input().split())
cook = int(input())

S += cook

if S >= 60:
    M += S // 60
    S = S % 60
if M >= 60:
    H += M // 60
    M = M % 60
if H >= 24:
    H = H % 24
print(H, M, S)
