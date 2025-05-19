A, B = map(int, input().split())
A -= 1
B -= 1
A_a = A // 4
A_b = A % 4
B_a = B // 4
B_b = B % 4

print(abs(A_a - B_a) + abs(B_b - A_b))