import sys
N = int(sys.stdin.readline())
PEOPLE = list(map(int, sys.stdin.readline().split()))
PEOPLE.sort()
ans1 = 0
ans2 = 0
for i in PEOPLE:
    ans2 = ans2 + i
    ans1 = ans1 + ans2

print(ans1)