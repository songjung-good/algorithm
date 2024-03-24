score = [int(input()) for _ in range(8)]
ans = []
num_lst = [1, 2, 3, 4, 5, 6, 7, 8]
total = 0
for j in range(7):
  for i in range(7-j):
    if score[i] < score[i+1]:
      score[i], score[i+1] = score[i+1], score[i]
      num_lst[i], num_lst[i+1] = num_lst[i+1], num_lst[i]

ans = sorted(num_lst[:5])
total = sum(score[:5])
print(total)
print(*ans)