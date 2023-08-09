#1
T = int(input())

for tc in range(1, T + 1):
    str1 = input()
    str2 = input()
    str1_len = len(str1)
    str2_len = len(str2)

    ans = 0
    for i in range(0, str2_len - str1_len + 1):
        if str1[0:str1_len] == str2[i:i+str1_len]:
            ans = 1
            break
        else:
            ans = 0

    print(f'#{tc} {ans}')

#2
T = int(input())

for tc in range(1, T + 1):
    str1 = input()
    str2 = input()

    if str1 in str2:                    #1 if문과 in을 이용
        result = 1

    #2 result = 1 if str1 in str2 else 0   #2 삼향조건연산자 A if 비교문 else B: 비교문 맞으면 A 틀리면 B

    print(f'#{tc} {result}')

    #3 print(int(str1 in str2))         #3 true와 false는 1과 0이므로


'''
특정 단어가 문장 내에 몇개 있는지 탐색  
#4

T = int(input())

for tc in range(1, T+1):
    str1 = input()
    str2 = input()
    str1_len = len(str1)
    str2_len = len(str2)
    ans = 0

    for i in range(str2_len - str1_len + 1):
        if str2[i] == str1[0]:
            k = 0
            while k < str1_len:
                if str1[k] == str2[i+k]:
                    if k == str1_len - 1:
                        ans += 1
                    k += 1
                elif str1[k] != str2[i+k]:
                    break

    print(f'#{tc} {ans}')
'''