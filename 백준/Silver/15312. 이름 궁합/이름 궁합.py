alt_num = [3, 2, 1, 2, 3, 3, 2, 3, 3, 2, 2, 1, 2, 2, 1, 2, 2, 2, 1, 2, 1, 1, 1, 2, 2, 1]
A = input()
B = input()

C = []
for i in range(len(A)):
    C.append(alt_num[ord(A[i]) - 65])
    C.append(alt_num[ord(B[i]) - 65])


while len(C) > 2:
    NEW = []
    for i in range(1, len(C)):
        NEW.append((C[i-1] + C[i]) % 10)
    C = NEW

print(C[0], C[1], sep='')
