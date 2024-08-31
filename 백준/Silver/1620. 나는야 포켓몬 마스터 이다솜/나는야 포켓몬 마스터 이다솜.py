N, M = map(int, input().split())

# 포켓몬 이름과 번호를 저장하는 딕셔너리
poke_dict = {}
# 포켓몬 번호와 이름을 저장하는 리스트
poke_list = [0]

# 포켓몬 정보 입력받기
for i in range(1, N + 1):
    poke_name = input()
    poke_dict[poke_name] = str(i)
    poke_list.append(poke_name)

for _ in range(M):
    quiz = input()
    if quiz.isdigit():
        ans = poke_list[int(quiz)]
    else:
        ans = poke_dict[quiz]
    print(ans)

