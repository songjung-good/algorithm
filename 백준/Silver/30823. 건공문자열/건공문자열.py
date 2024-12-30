N, K = map(int, input().split())
word = input()

if K == 1:
    print(word)
else:        
    if (N + K) % 2 == 1:
        print(word[K-1:] + word[:K-1])
    else:
        print(word[K-1:] + word[K-2::-1])
        