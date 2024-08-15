check = ['a','e','i','o','u']
word = input()
ans = 0
for i in word:
    if i in check:
        ans = ans + 1
        
print(ans)