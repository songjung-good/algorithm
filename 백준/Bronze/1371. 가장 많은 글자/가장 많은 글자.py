import sys

char_count = {}

# 입력값을 한 번에 읽기
word = sys.stdin.read()

# 문자 개수 세기
for w in word:
    if w not in (' ', '\n'):  # 공백과 개행 문자 제외
        char_count[w] = char_count.get(w, 0) + 1

# 가장 많이 등장한 문자 찾기
max_count = max(char_count.values())

# 등장 횟수가 max_count인 문자들 출력 (사전 순 정렬)
result = sorted([k for k, v in char_count.items() if v == max_count])
print(''.join(result))
