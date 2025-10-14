import sys
input = sys.stdin.readline

A, B, C = map(int, input().split())

def solv(A, B, C):
    if B == 1:
        return A % C

    else:
        temp = solv(A, B // 2, C)
        if B % 2:
            return (temp * temp) % C * A % C
        else:
            return (temp * temp) % C

print(solv(A, B, C))