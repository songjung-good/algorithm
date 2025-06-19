N = int(input())
lst= list(map(int, input().split())) 
even = 0
odd = 0
for n in range(N):
    if lst[n] % 2:
        odd += 1
    else:
        even += 1
if even > odd:
    print('Happy')
else:
    print('Sad')