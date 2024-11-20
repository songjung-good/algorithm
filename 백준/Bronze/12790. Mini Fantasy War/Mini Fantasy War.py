T = int(input())
for t in range(T):
    HP, MP, AT, DT, HPt, MPt, ATt, DTt = map(int, input().split())
    ans = max((HP + HPt), 1) + max((MP + MPt), 1) * 5 + max((AT + ATt), 0) * 2 + (DT + DTt) * 2
    print(ans)
