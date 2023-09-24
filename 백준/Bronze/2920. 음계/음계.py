A = input().strip().split()
past = ''
if int(A[0]) == 1:
    past = 'ascending'
    for i in range(1, 8):
        if int(A[i]) - int(A[i-1]) != 1:
            past = 'mixed'
            break
elif int(A[0]) == 8:
    past = 'descending'
    for i in range(1, 8):
        if int(A[i-1]) - int(A[i]) != 1:
            past = 'mixed'
            break
else:
    past = 'mixed'
print(past)

