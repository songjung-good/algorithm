T = int(input())
for _ in range(T):
    R, S = map(str, input().split())
    new_word = ''
    for i in S:
        new_word+=i*int(R)

    print(new_word)
