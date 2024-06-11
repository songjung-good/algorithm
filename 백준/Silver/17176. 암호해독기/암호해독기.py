def find_key(num):
    if num == 0:
        check = ' '
    elif num < 27:
        check = chr(num+64)
    else:
        check = chr(num+70)
    return check

N = int(input())
code = list(map(int, input().split()))
word = input()
ans = 'y'

cnt = {}
for char in word:
    if char in cnt:
        cnt[char] += 1
    else:
        cnt[char] = 1


for i in code:
    now = find_key(i)
    if now in cnt:
        if cnt[now] == 0:
            ans = 'n'
        else:
            cnt[now] -= 1
    else:
        ans = 'n'

if sum(cnt.values()) != 0:
    ans = 'n'

print(ans)