# 코드를 작성해주세요
N = int(input())
word = input()
ans = 0
for w in word:
    if w in ['a', 'e', 'i', 'o', 'u']:
       ans += 1
    
print(ans) 
    