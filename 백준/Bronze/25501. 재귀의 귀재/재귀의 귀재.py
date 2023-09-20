def recursion(s, l, r):
    global cnt
    cnt += 1
    if l >= r: return 1
    elif s[l] != s[r]: return 0
    else: return recursion(s, l+1, r-1)

def isPalindrome(s):
    return recursion(s, 0, len(s)-1)


A = int(input())
for i in range(A):
    cnt = 0
    B = input()
    cnt_1 = isPalindrome(B)
    print(cnt_1, cnt)


