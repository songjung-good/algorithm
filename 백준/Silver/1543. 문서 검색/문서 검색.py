A = input()
B = input()
n_A, n_B = len(A), len(B)
gap = n_A - n_B

ans = 0
if gap == 0:
    if A == B:
        ans += 1
else:
    for i in range(gap):
        start, end = i, i + n_B
        cnt = 0
        while start <= gap:
            if A[start:end] == B:
                cnt += 1
                start, end = end, end + n_B
            else:
                start, end = start+1, end+1
        if ans < cnt:
            ans = cnt
print(ans)