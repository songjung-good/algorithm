def change(i):
    if i in number:
        n = int(i)
    else:
        n = word[i]
    return n

num = input()
number = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
word = {
    'A' : 10,
    'B' : 11,
    'C' : 12,
    'D' : 13,
    'E' : 14,
    'F' : 15,
    }

ans = 0
size = len(num)
for i in num:
    n = change(i)
    size -= 1
    s = 16 ** size
    ans += n * s

print(ans)