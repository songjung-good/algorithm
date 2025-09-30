import sys
input = sys.stdin.readline

word = str(input().strip())
bomb = str(input().strip())
bomb_len = len(bomb)

ans = []
for w in word:
    ans.append(w)
    if len(ans) >= bomb_len:
        word = ''.join(ans[-bomb_len:])
        if word == bomb:
            for _ in range(bomb_len):
                ans.pop()

answer = ''.join(ans)
if answer == '':
    print('FRULA')
else:
    print(answer)
