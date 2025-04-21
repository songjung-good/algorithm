import sys
input = sys.stdin.readline

N = int(input())
lst = [int(input()) for _ in range(N)]
lst.sort()
dict = {}

print(int(round(sum(lst) / N, 0)))

print(lst[N//2])

keys=[]
for i in lst:
    if i in dict:
        dict[i] += 1
    else:
        dict[i] = 1
D = max(dict.values())
for k, v in dict.items():
    if v == D:
        keys.append(k)
if len(keys) > 1:
    print(keys[1])
else:
    print(keys[0])

print(lst[-1] - lst[0])