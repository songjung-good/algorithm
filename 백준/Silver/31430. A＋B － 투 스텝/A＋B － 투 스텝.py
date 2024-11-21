def change(C):
    # 숫자를 25진법으로 변환
    result = ""
    while C > 0:
        c = C % 26
        result = chr(c + 97) + result  # ord(a) = 97
        C //= 26
    return result

N = int(input())
# 갑
if N == 1:
    A, B = map(int, input().split())
    C = A + B
    ans = change(C)
    # 길이 13이 되도록 추가
    ans = 'a' * (13 - len(ans)) + ans
    print(ans)
# 을
elif N == 2:
    word = input()
    C = 0
    # 25진법 해석
    for i, char in enumerate(word[::-1]):
        C += (ord(char) - 97) * (26 ** i)
    print(C)

else:
    pass