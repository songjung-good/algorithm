# import sys
# input = sys.stdin.readline

N=int(input())
for _ in range(N):
    word = input()
    num = len(word)
    ans = 'Yes'
    for n in range(N//2):
        A = ord(word[n])
        B = ord(word[-1-n])
        if 97 <= A <= 122:
            A = A - 32
        if 97 <= B <= 122:
            B = B - 32
        if A == B:
            pass
        else:
            ans = 'No'
            break
    print(ans)
