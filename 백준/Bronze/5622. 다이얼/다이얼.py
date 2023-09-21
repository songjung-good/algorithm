A = input()
ans = 0
for i in A:
    if i in "ABC":
       ans += 3
    elif i in "DEF":
       ans += 4
    elif i in "GHI":
       ans += 5
    elif i in "JKL":
       ans += 6
    elif i in "MNO":
       ans += 7
    elif i in "PQRS":
       ans += 8
    elif i in "TUV":
       ans += 9
    elif i in "WXYZ":
       ans += 10
print(ans)