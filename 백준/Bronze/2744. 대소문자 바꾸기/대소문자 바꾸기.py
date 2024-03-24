A= input()
ans = ''
for i in A:
    if i.isupper():
        ans += i.lower()
    else:
        ans += i.upper()
print(ans)