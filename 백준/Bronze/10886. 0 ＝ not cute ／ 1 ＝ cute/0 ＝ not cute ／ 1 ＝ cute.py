N=int(input())
ans=0
for _ in range(N):
    A=int(input())
    if A:
        ans+=1
if N//2 < ans:
    print("Junhee is cute!")
else:
    print("Junhee is not cute!")