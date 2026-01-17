a, b, c = map(int, input().split())
d, e = map(int, input().split())

p2 = a * d * d
p1 = 2 * a * d * e + b * d
p0 = a * e * e + b * e + c

q2 = d * a
q1 = d * b
q0 = d * c + e

A = p2 - q2
B = p1 - q1
C = p0 - q0

if A == 0 and B == 0 and C == 0:
    print("Nice")
    exit()
    
if A != 0:
    D = B * B - 4 * A * C
    if D > 0:
        print("Go ahead")
    elif D == 0:
        print("Remember my character")
    else:
        print("Head on")
elif B != 0:
    print("Remember my character")
else:
    print("Head on")