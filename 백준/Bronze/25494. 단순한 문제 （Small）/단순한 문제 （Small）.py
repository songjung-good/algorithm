# 코드를 작성해주세요
T = int(input())
for _ in range(T):
    a, b, c = map(int, input().split())
    x=min(a,b,c)
    print(x)
    