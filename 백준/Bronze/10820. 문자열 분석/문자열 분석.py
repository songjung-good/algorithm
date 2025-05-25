while True:
    try:
        ans = [0, 0, 0, 0]
        word = input()
        for w in word:
            if w == ' ':
                ans[3] += 1
            elif w in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                ans[2] += 1
            elif 65 <= ord(w) <= 90:
                ans[1] += 1
            elif 97 <= ord(w) <= 122:
                ans[0] += 1
        print(*ans)
    except:
        exit()