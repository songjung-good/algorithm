K = int(input())
word = input()
map = []

check = 1
new_word = []
cnt = 0
for w in word:
    if check == 1:
        new_word.append(w)
    elif check == -1:
        new_word.insert(0, w)
    cnt += 1
    if cnt == K:
        map.append(new_word)
        cnt = 0
        check = check * -1
        new_word = []

for k in range(K):
    for m in map:
        print(m[k], end='')