'''
    괄호의 순서 고려
    남았는지 안남았는지 고려

    대괄호 중괄호 소괄호의 각자 스택을 만들고
    현재 진행 스택이 닫히기 전에 이전 스택이 먼저 닫히면 0출력
    남은 스택이 있을경우 0출력
    스택이 -1 보다 작으면 0출력
'''

'''
해당 방식은 pop할 때 순서를 정하는 과정이 복잡할 것으로 예상
#1
def push(str, size):
    global top
    top = -1
    top1 = top2 = top3 = top
    stack = [0] * size
    stack1 = stack2 = stack = stack
    
    for i in range(size):
        if str[i] is '('or ')':
            top1 += 1
            stack1[top1] = i
        elif str[i] is '{' or '}':
            top2 += 1
            stack2[top2] = i
        elif str[i] is '[' or ']':
            top3 += 1
            stack2[top3] = i
            
T = int(input())
for tc in range(1, T+1):
    case_str = input()
    case_size= len(case_str)
'''
#2 한개의 스택에 다 담고 순서대로 내보낸다.


def push(str_c, size):
    top = -1
    stack = [0] * size
    ans = 1

    for i in range(size):
        # if str_c[i] == '(' or str_c[i] == ')' or str_c[i] == '{' or str_c[i] == '}'or str_c[i] == '[' or str_c[i] == ']':
        if str_c[i] in '({[':
            top += 1
            stack[top] = str_c[i]
        elif str_c[i] in ')}]':
            if stack[top] != str_c[i]:
                ans = 0
            elif stack[top] == str_c[i]:
                top -= 1

    return ans

T = int(input())
for tc in range(1, T+1):
    case_str = input()
    case_size = len(case_str)
    print(push(case_str, case_size))
