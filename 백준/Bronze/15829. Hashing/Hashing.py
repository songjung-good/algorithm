L = int(input())
WORD = str(input())

r = 31
M = 1234567891
ans = 0

for idx, i in enumerate(WORD):
    number = ord(i) - 96
    ans = (ans + number * (r ** idx)) % M

print(ans)