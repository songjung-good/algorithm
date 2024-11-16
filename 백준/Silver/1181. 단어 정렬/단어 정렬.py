N = int(input())
words = set()

for n in range(N):
    word = input()
    words.add(word)

sorted_words = sorted(words, key=lambda x: (len(x), x))

for s in sorted_words:
    print(s)