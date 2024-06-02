NUM_LST = []
for i in range(5):
    A = int(input())
    if i == 0:
        NUM_LST.append(A)
    else:
        for j in range(i):
            if A <= NUM_LST[j]:
                NUM_LST.insert(j, A)
                break
            elif j == (i-1):
                NUM_LST.append(A)

ans1 = sum(NUM_LST) // 5
ans2 = NUM_LST[2]

print(ans1)
print(ans2)