imo = input()
A = 0
B = 0
C = 0
for i in imo:
    A = A + 1
    if i == ':':
        B = B + 1
    elif i == '_':
        C = C + 1

ans = A + B + C * 5
print(ans)
