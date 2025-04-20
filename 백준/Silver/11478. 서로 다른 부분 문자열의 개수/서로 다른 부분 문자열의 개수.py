# import sys
# input = sys.stdin.readline

lst = set()
word = input()
for i in range(len(word)):
    for j in range(i+1, len(word)+1):
        lst.add(word[i:j])

print(len(lst))