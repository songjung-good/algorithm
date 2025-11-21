T = int(input())
for _ in range(T):
    input()
    # 8, 8, 4, 1, 9 => 16
    Cm, y, Ssu, Ssa, f = map(int, input().split())
    # 1, 30, 25, 10
    b, Gs, Gc, w = map(int, input().split())

    Cm, y, Ssu, Ssa, f = Cm/8, y/8, Ssu/4, Ssa, f/9
    b, Gs, Gc, w = b, Gs//30, Gc//25, w//10

    cake_mix = int(min(Cm, y, Ssu, Ssa, f) * 16)
    cake_top = sum([b, Gs, Gc, w])
    if cake_mix > cake_top:
        print(cake_top)
    else:
        print(cake_mix)
