from itertools import combinations, permutations
from collections import deque
word = deque(input())
ans = ''

vowel = ['a', 'e', 'i', 'o', 'u']
while word:
    now=word.popleft()
    if now in vowel:
        word.popleft()
        word.popleft()
    ans += now

print(ans)