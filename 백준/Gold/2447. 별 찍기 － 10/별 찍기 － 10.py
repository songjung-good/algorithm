def make_star(n):
    if n == 1:
        return ['*']

    star = make_star(n//3)
    new_star = []

    for s in star:
        new_star.append(s*3)
    for s in star:
        new_star.append(s + ' '*(n//3) + s)
    for s in star:
        new_star.append(s*3)
    return new_star

N=int(input())
print('\n'.join(make_star(N)))