import sys
input = sys.stdin.readline

N, M = map(int, input().split())
dic = {}
for _ in range(N):
    word = input().rstrip()
    cnt = len(word)
    if cnt >= M:
        if word in dic:
            dic[word][0] += 1
        else:
            dic[word] = [1, cnt]

sort_dic = sorted(dic.items(), key = lambda i: (-i[1][0], -i[1][1], i[0]))

for word, _ in sort_dic:
    print(word)
