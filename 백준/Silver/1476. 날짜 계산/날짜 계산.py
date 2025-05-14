E, S, M = map(int, input().split())
A, B, C = 0, 0, 0
while True:
    X, Y, Z = (A * 15) + E, (B * 28) + S, (C * 19) + M
    if X != Y:
        if X > Y:
            B += 1
        else:
            A += 1
    else:
        if Y != Z:
            if Y > Z:
                C += 1
            else:
                B += 1
    if X == Y == Z:
        break
print(X)