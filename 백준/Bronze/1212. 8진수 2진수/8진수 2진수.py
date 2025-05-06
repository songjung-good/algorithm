import sys
input = sys.stdin.readline

# 8진수 입력
octa = input().strip()

# 8진수 0일 경우 바로 출력
if octa == '0':
    print(0)
else:
    # 8진수를 10진수로 변환 후 2진수로 변환
    ans = bin(int(octa, 8))[2:]
    print(ans)