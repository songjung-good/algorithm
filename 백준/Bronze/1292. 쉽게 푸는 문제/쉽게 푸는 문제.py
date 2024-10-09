num_lst = []
cnt = 0
for A in range(1, 100):
    for a in range(A):
        num_lst.append(A)

x, y = map(int, input().split())

print(sum(num_lst[x-1:y]))