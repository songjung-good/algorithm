#1
'''
T = int(input())

for tc in range(1, T+1):
    str1 = input()
    str2 = input()
    str1_len = len(str1)
    str2_len = len(str2)
    ans = 0
    cnt = 0

    for i in range(str1_len):
        for j in range(str2_len):
            if str1[i] == str2[j]:
                cnt += 1
        if ans < cnt:
            ans = cnt
        cnt = 0

    print(f'#{tc} {ans}')
'''

#2
T = int(input())

for t in range(1, T + 1):
    str1 = set(input())
    str2 = input()

    # for s1 in str1:
    #     print(s1, end = " ")
    # print()
    DICT = dict.fromkeys(str1, 0)

    for s1 in str1:
        for s2 in str2:
            if s1 == s2:
                DICT[s1] += 1

    # print(DICT)

    result = max(DICT.values())

    print(f'#{t} {result}')


#3
T = int(input())

for t in range(1, T + 1):
    str1 = input()
    str2 = input()
    lst = []

    for s1 in str1:
        lst.append(str2.count(s1))

    result = max(lst)

    print(f'#{t} {result}')