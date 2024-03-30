N = int(input())
divisors = list(map(int, input().split()))

# 주어진 약수들을 오름차순으로 정렬합니다.
divisors.sort()

# 가장 작은 약수와 가장 큰 약수를 곱하여 원래 수를 구합니다.
original_number = divisors[0] * divisors[-1]

print(original_number)
