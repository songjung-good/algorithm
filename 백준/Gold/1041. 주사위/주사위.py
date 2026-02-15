N = int(input())
lst = list(map(int, input().split()))

# 값이 작은 조합
comb = [min(lst[0], lst[5]),
       min(lst[1], lst[4]),
       min(lst[2], lst[3])]
comb.sort()
tri = sum(comb) * 4
duo = comb[0] + comb[1]

if N == 1:
    print(sum(lst) - max(lst))
else:
    num = (N - 2)
    print(tri + duo * (4 + num * 8) + min(lst) * ((num ** 2 * 5) + (num * 4)))
