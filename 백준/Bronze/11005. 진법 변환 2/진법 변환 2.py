'''
N, B = map(str, input().split())
num_lst = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
ans = 0
cnt = 0
for i in N[::-1]:
    line = int(B) ** cnt
    if i not in num_lst:
        ans += (ord(i) - 55) * line
    else:
        ans += int(i) * line
    cnt += 1
print(ans)
'''

N, B = map(int, input().split())
num = N
ans = ''
while num:
    new_num = num % B
    if new_num > 9:
        new_word = chr(new_num + 55)
        new_word += ans
        ans = new_word
    else:
        new_word = str(new_num)
        new_word += ans
        ans = new_word
    num = num // B
print(ans)