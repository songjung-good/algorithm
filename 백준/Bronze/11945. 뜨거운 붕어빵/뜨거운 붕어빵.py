# 코드를 작성해주세요
N, M = map(int, input().split())
for _ in range(N):
    word = input()
    for i in range(M):
        print(word[M-1-i], end='')
    print()
    