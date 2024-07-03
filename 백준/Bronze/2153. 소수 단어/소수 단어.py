import math

def prime_num(X):
    for i in range(2, int(math.sqrt(X)) + 1):
        if X % i == 0:
            return False
    return True

# 97 = a 65 = A
# print(ord("a"))
# print(chr(65))

WORD = input()
NUMBER = 0
for i in WORD:
    alt = ord(i)
    if alt >= 97:
        alt -= 96
    else:
        alt -= 38
    NUMBER += alt

M = prime_num(NUMBER)

if M:
    ans="a"
else:
    ans="not a"

print("It is ", end="")
print(ans, end="")
print(" prime word.")