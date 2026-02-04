K = int(input())
N = int(input())
time = 210
for _ in range(N):
    T, Z = input().split()
    time -= int(T)
    if time <= 0:
        break
    else:
        if Z == 'T':
            K += 1
            if K == 9:
                K = 1

print(K)
