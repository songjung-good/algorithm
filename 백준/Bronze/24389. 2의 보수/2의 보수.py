N = int(input())

# 32비트 표현 유지
mask = (1 << 32) - 1

# 2의 보수 계산
M = (~N + 1) & mask

# N XOR M의 1의 개수 = 변한 비트 수
print(bin(N ^ M).count('1'))