# 코드를 작성해주세요
word = input()

for i in word:
    num = ord(i)
    ans = 0
    while num:
        ans += num%10
        num //= 10        
    print(i*ans)