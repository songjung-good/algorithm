# 코드를 작성해주세요
import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    A, B = input().split()
    A, B = list(A), list(B)
    cnt = len(A)
    ans = 0

    # A와 B의 길이가 다른경우
    if cnt != len(B):
        ans = -1
        continue

    # A와 B가 같은 지 하나씩 확인
    for n in range(cnt):
        if A[n] != B[n]:
            if n == cnt-1:
                ans = -1

            # 다르면 같은 인덱스 찾아서 데려오기
            else:
                for m in range(n+1, cnt):
                    if A[m] == B[n]:
                        ans += m-n
                        A[n], A[n+1:m+1] = A[m], A[n:m]
                        break

    print(ans)