K = int(input())
num_lst = [int(input()) for _ in range(K)]
ans_lst = []

cnt = -1
for i in num_lst:
  if i > 0:
    cnt += 1
    ans_lst.append(i)
  else:
    ans_lst.pop()
    cnt -= 1

answer = sum(ans_lst)
print(answer)