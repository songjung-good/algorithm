A, B = map(str, input().split())

minA = ''
minB = ''
maxA = ''
maxB = ''

for a in A:
    if a == '6':
        minA += '5'
        maxA += a
    elif a == '5':
        maxA += '6'
        minA += a
    else:
        maxA += a
        minA += a
        
for b in B:
    if b == '6':
        minB += '5'
        maxB += b
    elif b == '5':
        maxB += '6'
        minB += b
    else:
        maxB += b
        minB += b

X = int(minA) + int(minB)
Y = int(maxA) + int(maxB)

print(*[X, Y])