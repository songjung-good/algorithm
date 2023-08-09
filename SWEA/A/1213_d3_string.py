'''
    1번 방법
    문장의 뒤에서 부터 탐색하여

    글자가 다르면 해당 글자의 길이만큼 문장이동
'''
# for tc in range(1, 11):
#     input()
#     find_str = input()
#     search_str = input()
#
#     A = len(search_str)
#     B = len(find_str)
#     while A > 0:
#         i = 0
#         A -= i
#         if find_str[-1] == search_str[-i-1]:
#             for j in range(B):
#                 if find_str[-j-1] != search_str[-i-1-j]:
#                     i += j
#
#
#     print(f'#{tc} {find_str}')
    # print(search_str)
    #
    # print(type(find_str))
    # print(type(search_str))


'''
    2번 방법
    앞에서 부터 탐색
    찾을 문자열의 0번 인덱스를 검색할 문장에서 찾으면
    해당 칸을 1로 치환
    1 ~ 찾을 문자열의 수까지 바뀌면 탐색수 1 증가
'''
'''
for tc in range(1, 11):
    input()
    find_str = list(map(str, input()))
    search_str = list(map(str, input()))

    A = len(find_str)
    B = len(search_str)
    i = 0
    while i < B - A + 1:
        if find_str[0] == search_str[i]:
            search_str[i] = 1
            for j in range(1, A):
                if find_str[j] == search_str[j+i]:
                    search_str[j+i] = j + 1
                else:
                    search_str[j + i] = 0
                    i += j
                    break
        else:
            search_str[i] = 0
            i += 1

    print(f'#{tc} {search_str}')

'''



#3
for tc in range(1, 11):
    input()
    find_str = list(map(str, input()))
    search_str = list(map(str, input()))

    A = len(find_str)
    B = len(search_str)
    ans = 0
    for i in range(B-A+1):

        j = 0
        while j < A:
            if search_str[i + j] != find_str[j]:
                break
            j += 1
        if j == A:
            ans += 1

    print(f'#{tc} {ans}')