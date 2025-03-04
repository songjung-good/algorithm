import math

N = int(input())
A = sum(list(map(int,input().split())))
B = sum(list(map(int,input().split())))

cnt = float('inf')
num = math.lcm(A,B)

print(num//A, num//B, sep=' ')
