R, B = map(int, input().split())

size = R+B
ROW = 0
COL = 0

if B > 0:
    for i in range(3, R):
        if size % i != 0:
            pass
        else:
            j = size // i
            if (i-2) * (j-2) == B:
                ROW = i
                COL = j
                break
        if ROW != 0:
            break

ans = [ROW, COL]
ans.sort(reverse=True)
print(*ans)
