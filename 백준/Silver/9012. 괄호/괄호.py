A = int(input())  # 테스트 케이스의 개수를 입력 받습니다.

for _ in range(A):
    B = input()  # 괄호 문자열을 입력 받습니다.
    ans = 'NO'  # 초기에 결과를 'NO'로 설정합니다.
    cnt = 0  # 괄호의 개수를 세는 변수를 초기화합니다.
    for i in B:
        if i == ')':
            cnt -= 1  # 여는 괄호에 대응하는 닫는 괄호를 하나 제거합니다.
        else:
            cnt += 1  # 여는 괄호가 나오는 경우 괄호의 개수를 하나 더합니다.
        if cnt < 0:
            break
    if cnt == 0:  # 모든 여는 괄호에 대응하는 닫는 괄호가 있을 때
        ans = 'YES'  # 결과를 'YES'로 설정합니다.
    print(ans)  # 결과를 출력합니다.