X, Y = map(int, input().split())

# 듣도 못한 사람들 집합
not_heard = set(input().strip() for _ in range(X))

# 보도 못한 사람들 집합
not_seen = set(input().strip() for _ in range(Y))

# 교집합 구하기
not_heard_seen = sorted(not_heard & not_seen)

# 결과 출력
print(len(not_heard_seen))
for name in not_heard_seen:
    print(name)
