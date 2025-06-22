N = int(input())
for _ in range(N):
    word=input()
    if word[:10] == "Simon says":
        print(word[10:])