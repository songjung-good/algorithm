a = int(input())
word = ""

if a == 1 or a % 2 == 1:
    word = "odd"
else:
    word = "even"

ans = str(a) + " is " + word 

print(ans)