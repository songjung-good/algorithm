# 입력 전부 받아오기
# 1. readlines 이용하기
'''
import sys
ALL = sys.stdin.readlines()
'''

# 2. while 이용하기
while True:
    try:
        WORD = input()
        ans = 'yes'
        stack = []
        if WORD != '.':
            for i in WORD:
                if i == '.' or ans == 'no':
                    break
                if i == '[' or i == '(':
                    stack.append(i)
                elif i == ']':
                    if stack and stack[-1] == '[':
                        stack.pop(-1)
                    else:
                        ans = 'no'
                elif i == ')':
                    if stack and stack[-1] == '(':
                        stack.pop(-1)
                    else:
                        ans = 'no'
            if stack:
                ans = 'no'
            print(ans)
        else:
            pass
    except EOFError:
        break
