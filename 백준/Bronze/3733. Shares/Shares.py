while True:
    try:
        A, B = map(int, input().split())
        if A + 1 > B:
            print(0)
        else:
            ans = B // (A + 1)
            print(ans)
    except EOFError:
        break