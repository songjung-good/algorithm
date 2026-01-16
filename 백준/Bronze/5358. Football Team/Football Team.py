while True:
    try:
        word=input()
        ans = ''
        for w in word:
            if w == 'i':
                w = 'e'
            elif w == 'e':
                w = 'i'
            elif w == 'I':
                w = 'E'
            elif w == 'E':
                w = 'I'
            ans += w
        print(ans)
    except:
        break