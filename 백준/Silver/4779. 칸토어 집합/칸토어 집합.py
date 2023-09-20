'''
'-' 가 3**N개 있는 문자열
문자열을 3등분 가운데를 공백(" ")으로
모든 선의 길이가 1일 때까지
'''


# 문자열과 그 문자열의 길이
def canto(word, num):
    left = word[:num//3]
    mid = " " * (num//3)
    right = word[2*(num//3):]

    if num != 3:
       left = canto(left, num//3)
       right = canto(right, num//3)

    new_word = left+mid+right
    return new_word

while True:
    try:
        N=int(input())
        str_a = '-' * 3**N
        if N == 0:
            print(str_a)
        else:
            print(canto(str_a, 3**N))
    except:
        break
# print(str_a)
