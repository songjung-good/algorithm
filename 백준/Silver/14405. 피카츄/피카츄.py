word=input()
num=len(word)
start=0
while start < num:
    if word[start:start+2] in ['pi', 'ka']:
        start+=2
    elif word[start:start+3] == 'chu':
        start+=3
    else:
        print('NO')
        exit()
print('YES')