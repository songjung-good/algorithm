N, K = map(str, input().split())
player = {
    'Y' : 1,
    'F' : 2,
    'O' : 3,
}
last_players = []
div = player[K]

for n in range(int(N)):
    name = input()
    last_players.append(name)

last_players = set(last_players)
NUM = len(last_players)
ans = NUM // div
print(ans)
