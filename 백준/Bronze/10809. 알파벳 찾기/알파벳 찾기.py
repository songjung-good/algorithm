word = input()
lst = [-1] * 26

cnt = 1
for i in word:
    if lst[ord(i)-97] == -1:
        lst[ord(i) - 97] += cnt
    cnt += 1

print(*lst)