import sys
input = sys.stdin.readline

M = int(input())
S = [0] * 21
for i in range(M):
    word = input().strip().split()

    if word[0] == 'all':
        S = [1] * 21

    elif word[0] == 'empty':
        S = [0] * 21

    else:
        word[1] = int(word[1])
        if S[word[1]]:
            if word[0] == 'remove':
                S[word[1]] = 0
            elif word[0] == 'check':
                print('1')
            elif word[0] == 'toggle':
                S[word[1]] = 0

        else:
            if word[0] == 'add':
                S[word[1]] = 1
            elif word[0] == 'check':
                print('0')
            elif word[0] == 'toggle':
                S[word[1]] = 1