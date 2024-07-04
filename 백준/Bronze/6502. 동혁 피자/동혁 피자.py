num = 1
while True:
    try:
        r, w, l = map(int, input().split())
        size = (w / 2) ** 2 + (l / 2) ** 2
        r = r**2
        if size <= r:
            ans = "fits on the table."
        else:
            ans = "does not fit on the table."

        print(f"Pizza {num} {ans}")
        num += 1
    except:
        break