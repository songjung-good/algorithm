word = ['baby', 'sukhwan', 'tururu', 'turu', 'very', 'cute', 'tururu', 'turu', 'in', 'bed', 'tururu', 'turu', 'baby', 'sukhwan']
song = len(word)
CNT = int(input()) - 1  # 0-based index로 맞추기 위해 1을 뺍니다.

A = CNT % song
B = CNT // song

ans = word[A]
if ans == 'tururu':
    ans = f"tu+ru*{2+B}" if B >= 3 else ans + 'ru' * B
elif ans == 'turu':
    ans = f"tu+ru*{1+B}" if B >= 4 else ans + 'ru' * B

print(ans)
