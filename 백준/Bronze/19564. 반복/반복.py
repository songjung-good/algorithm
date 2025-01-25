word = input()
cnt = 1
past = 0
for w in word:
    now = ord(w)
    if past < now:
        pass
    else:
        cnt += 1
    past = now

print(cnt)
