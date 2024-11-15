def check(feet, inch):
    if inch >= 12:
        feet += inch // 12
        inch = inch % 12
    if inch < 0:
        feet -= 1
        inch += 12
    if feet % 2 == 1:
        feet = feet // 2
        inch += 12
    else:
        feet = feet // 2
    if inch % 2 == 1:
        inch1 = inch // 2 + 1
    else:
        inch1 = inch // 2

    inch2 = inch // 2
    feet1 = feet
    feet2 = feet

    inch1 -= 4
    inch2 += 4

    if inch1 < 0:
        feet1 -= 1
        inch1 += 12
    if inch2 >= 12:
        feet2 += 1
        inch2 -= 12

    return feet1, inch1, feet2, inch2

T = int(input())
for t in range(T):
    CASE = list(map(str, input().split()))
    SIZE = CASE[1] + CASE[2]
    # MOM = CASE[2]
    feet = 0
    inch = 0
    word = ''
    # print(DAD)
    for d in SIZE:
        if d == '\'':
            feet += int(word)
            word = ''
        elif d == '\"':
            inch += int(word)
            word = ''
        else:
            word += d
        # print(word)

    if CASE[0] == 'B':
        inch += 5
    else:
        inch -= 5

    a_feet, a_inch, b_feet, b_inch = check(feet, inch)

    print(f'Case #{t+1}: {a_feet}\'{a_inch}\" to {b_feet}\'{b_inch}\"')