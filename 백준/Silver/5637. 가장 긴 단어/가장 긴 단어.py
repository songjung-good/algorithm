# 코드를 작성해주세요
import sys, re

ans = ''

all_word = sys.stdin
for line in all_word:
    word = re.findall(r"[a-zA-Z-]+", line)
    for w in word:
        lower_word = w.lower()
        if len(lower_word) > len(ans):
            ans = lower_word

print(ans)
    