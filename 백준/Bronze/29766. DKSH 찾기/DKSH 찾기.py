word=input()
ans=0
cnt=len(word)
if cnt < 4:
    pass
else:
    for i in range(cnt-3):
        if word[i:i+4] == 'DKSH':
            ans += 1

print(ans)