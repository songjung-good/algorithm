# 코드를 작성해주세요
A = int(input())
W, V = map(int, input().split())
B = W // V
if B >= A:
    print(1)
else: 
    print(0)