N=int(input())
lst=list(map(int, input().split()))
time=(N-1) * 8 + sum(lst)
print(time//24, time%24)