T = int(input())

for _ in range(T):
    word = ''
    case = list(map(str, input().split()))
    for c in case:
        now = 0
        if len(c) == 1:
            word += c
        else:
            for x in c:
                now += ord(x) - 97
            now = now % 27
            if now == 26:
                word += ' '
            else:
                word += chr(now + 97)

    print(word)