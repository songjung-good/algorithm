days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
day_lst = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

D, M = map(int, input().split())
num = D + sum(days[:M-1])
print(day_lst[(num+2) % 7])