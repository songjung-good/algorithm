N=int(input())
ans=0
for _ in range(N):
    word=input()
    num=int(word[2:])
    if num > 90:
        pass
    else:
        ans+=1
print(ans)