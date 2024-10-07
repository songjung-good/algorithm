N = int(input())
for n in range(N):
    A = str(input())
    B = len(A) // 2
    if A[B] == A[B-1]:
        print("Do-it")
    else:
        print("Do-it-Not")
