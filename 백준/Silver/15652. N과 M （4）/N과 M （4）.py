'''
자연수 N과 M이 주어졌을 때,
아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.
1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열
'''

'''
#1
def select(arr, num, save_lst):
    stack = save_lst

    for i in arr:
        if i not in stack:
            stack.append(i)
        if len(stack) != num:
            select(arr, num, stack)
        elif len(stack) == num:
            print(" ".join(map(str, stack)))
            stack.pop(-1)


N, M = map(int, input().split())

lst = list(range(1, N+1))

ety_lst = []

select(lst, M, ety_lst)
'''

#1-1
def select(arr, num, n, stack=[]):
    if len(stack) == num:
        print(" ".join(map(str, stack)))
        return

    for i in arr[n:]:
        select(arr, num, i-1, stack + [i])

N, M = map(int, input().split())
lst = list(range(1, N+1))
select(lst, M, 0)



'''
#2
def generate_sequences(N, M, current_seq=[]):
    if len(current_seq) == M:
        print(" ".join(map(str, current_seq)))
        return

    for num in range(1, N + 1):
        if num not in current_seq:
            current_seq.append(num)
            generate_sequences(N, M, current_seq)
            current_seq.pop()

N, M = map(int, input().split())
generate_sequences(N, M)
'''

'''#3
def generate_sequences(N, M):
    stack = []  # 스택을 사용하여 현재까지의 수열을 저장

    while True:
        # 스택에 M개의 숫자가 쌓이면 출력
        if len(stack) == M:
            print(" ".join(map(str, stack)))

        # 스택이 비어있거나 마지막 숫자가 N보다 작다면 다음 숫자 추가
        if not stack or stack[-1] < N:
            if not stack:
                num = 1
            else:
                num = stack[-1] + 1
            stack.append(num)
        else:
            # 스택이 비어있지 않고 마지막 숫자가 N과 같거나 크면 마지막 숫자 제거
            stack.pop()

        # 스택이 비어있다면 모든 수열을 생성한 것이므로 종료
        if not stack:
            break

N, M = map(int, input().split())
generate_sequences(N, M)
'''