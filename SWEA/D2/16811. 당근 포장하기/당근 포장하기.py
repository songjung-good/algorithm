T = int(input())
for tc in range(1, 1+T):
    N = int(input())
    carrot_size = list(map(int, input().split()))
    ans = 9999
    carrot_size.sort()

    for i in range(N-2):
        for j in range(i+1, N-1):
            if carrot_size[i] != carrot_size[i+1] and carrot_size[j] != carrot_size[j+1]:
                small = i+1
                middle = j - i
                large = N - small - middle
                if small <= N//2 and middle <= N//2 and large <= N//2:
                    box = max(small, middle, large) - min(small, middle, large)
                    if ans > box:
                        ans = box
                    if ans == 0:
                        break

    if ans == 9999:
        ans = -1

    print(f'#{tc} {ans}')