x = []
y = []
for _ in range(3):
    A, B = map(int, input().split())
    if A in x:
        x.remove(A)
    elif A not in x:
        x.append(A)
    if B in y:
        y.remove(B)
    elif B not in y:
        y.append(B)
        
print(*x, end=" ")
print(*y)
        