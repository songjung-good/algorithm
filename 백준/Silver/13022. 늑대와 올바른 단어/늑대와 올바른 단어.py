word = input()
size = len(word)
if size % 4:
    print(0)
    exit()
else:
    start = 0
    end = 0
    now = 1
    while start < size:
        check_word = ''
        if end > size:
            print(0)
            exit()
        for i in 'wolf':
            check_word += i * now

        end = start + (now*4)
        if word[start:end] == check_word:
            start = end
            now = 1
        else:
            now += 1

print(1)