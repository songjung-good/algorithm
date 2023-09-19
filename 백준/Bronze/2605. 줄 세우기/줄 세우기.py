N = int(input())
line = [i+1 for i in range(N)]
num_lst = list(map(int, input().split()))
new_line = []
for i in range(N):
    new_line.insert(i-num_lst[i], line[i])

print(*new_line)