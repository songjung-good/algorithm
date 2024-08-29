ham = []
drink = []

for i in range(3):
    menu = int(input())
    ham.append(menu)

for j in range(2):
    menu1 = int(input())
    drink.append(menu1)

ans = min(ham) + min(drink) - 50

print(ans)