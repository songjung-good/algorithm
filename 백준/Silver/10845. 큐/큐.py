# 코드를 작성해주세요
import sys
input = sys.stdin.readline

N = int(input())
Q = []
CNT = 0

for n in range(N):
    order_line = list(map(str, input().split()))
    order = order_line[0]
    
    if order == 'push':
        Q.append(int(order_line[1]))
        CNT += 1
        
    elif order == 'pop':
        if CNT:
            print(int(Q.pop(0)))
            CNT -= 1
        else:
            print(-1)
            
    elif order == 'size':
        print(CNT)
        
    elif order == 'empty':
        if CNT:
            print(0)
        else:
            print(1)
            
    elif order == 'front':
        if CNT:
            print(Q[0])
        else:
            print(-1)
    elif order == 'back':
        if CNT:
            print(Q[-1])
        else:
            print(-1)