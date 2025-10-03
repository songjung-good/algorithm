A = int(input())
B = int(input())

ans = B - A
if ans < 0:
    ans += 24
    
print(ans)