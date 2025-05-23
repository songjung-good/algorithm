small = 'roygbvi'
big = 'ROYGBVI'
N = int(input())
word = input()
A, B, C = True, True, False
for s in small:
    if not s in word:
        A = False

for b in big:
    if not b in word:
        B = False

if A and B:
    print('YeS')
elif A:
    print('yes')
elif B:
    print('YES')
else:
    print('NO!')
