from fractions import Fraction

X, Y = map(int, input().split())
if X - Y <= 0:
    print(-1)
else:
    Z = int(Fraction(Y, X) * 100)
    if Z == 99:
        print(-1)
    else:
        start = 0
        end = X
        while start < end:
            mid = (start+end) // 2
            now = int(Fraction((Y + mid), (X + mid)) * 100)
            if Z >= now:
                start = mid + 1
            else:
                end = mid

        print(start)
