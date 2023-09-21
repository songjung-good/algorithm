word=input()
past_word = ''
ed = len(word)-1
now = 0

cnt = 0
cro_alp = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
while now <= ed:
    if now != ed-1 and word[now:now+3] == 'dz=':
        cnt += 1
        now += 3
    elif word[now:now+2] in cro_alp:
        cnt += 1
        now += 2
    else:
        now += 1
        cnt += 1

print(cnt)
