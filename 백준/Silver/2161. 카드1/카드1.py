num = int(input())
deck = []
ans = []
now = 0
for i in range(num):
    if now == 0:
        now += 1
        ans.append(i+1)
        pass
    else:
        now -= 1
        deck.append(i+1)

while deck:
    card = deck.pop(0)
    if now == 0:
        now += 1
        ans.append(card)
        pass
    else:
        now -= 1
        deck.append(card)


print(*ans)

