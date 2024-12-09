import sys
input = sys.stdin.readline

EX = input().strip()  # 개행 문자 제거

num_lst = []  # '-'로 분리된 숫자 그룹을 저장
number = ''  # 현재 숫자를 저장할 임시 변수

for n in EX:
    if n == '-':  # '-'를 만나면 현재 숫자 그룹을 종료하고 추가
        num_lst.append(sum(map(int, number.split('+'))))  # '+'로 구분된 숫자 합산
        number = ''  # 초기화
    else:
        number += n  # 숫자나 '+'를 계속 추가

# 마지막 숫자 그룹 처리
num_lst.append(sum(map(int, number.split('+'))))

# 첫 번째 숫자 그룹에서 나머지를 뺀다
ans = num_lst[0]
for n in num_lst[1:]:
    ans -= n

print(ans)