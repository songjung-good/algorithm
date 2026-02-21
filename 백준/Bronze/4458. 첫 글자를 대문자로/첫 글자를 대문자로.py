N=int(input())
for _ in range(N):
    word = input()
    ans = word[0].upper() + word[1:]
    print(ans)