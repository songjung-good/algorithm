# 참가자 N명
N = int(input())
# 티셔츠 사이즈
SHIRT= list(map(int, input().split()))
# 펜 주문 단위 P, 티셔츠 주문 단위 T
T, P = map(int, input().split())

ans1 = 0
for i in SHIRT:
    if i == 0:
        pass
    elif T > i:
        ans1 += 1
    else:
        NUM = i // T
        ans1 += NUM
        if i % T == 0:
            pass
        else:
            ans1 += 1

# 펜 구매 수
if N < P:
    ans2 = [0, N]
else:
    if N % P == 0:
        ans2 = [N // P, 0]
    else:
        ans2 = [N // P, N % P]

print(ans1)
print(*ans2)