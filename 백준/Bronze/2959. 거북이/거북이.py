# 코드를 작성해주세요
lst = list(map(int, input().split()))
lst.sort()

print(min(lst[0], lst[1]) * min(lst[2], lst[3]))