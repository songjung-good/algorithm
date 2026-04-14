# 코드를 작성해주세요
D=input()
past = ''
ans = 0
for i in D:
    if i == past:
        ans += 5
    else:
        ans += 10
    past = i

print(ans)