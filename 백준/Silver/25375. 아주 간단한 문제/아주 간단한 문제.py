'''
두 수의 최대공약수로, 두 수의 합을 나눌 수 있다
임의의 두 자연수 x, y
두 수의 최대공약수 a
두 수의 합 b
x = a * q, y = a * p
b = a * (q + p)
'''
import sys, math
input = sys.stdin.readline

Q = int(input())
for _ in range(Q):
    ans = 0
    # gcd(x,y) = a, x+y = b
    a, b = map(int, input().split())
    if b % a == 0 and b // a >= 2:
        ans = 1
    print(ans)