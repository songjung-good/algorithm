# 코드를 작성해주세요
for n in range(1, int(input())+1):
    G = list(map(int, input().split()))
    S = list(map(int, input().split()))
    G_s = [1,2,3,3,4,10]
    S_s = [1,2,2,2,3,5]
    G_score, S_score = 0, 0
    for i in range(6):
        G_score += G[i]*G_s[i]
        S_score += S[i]*S_s[i]
    S_score += S[-1] * 10
    
    if G_score > S_score:
        print(f"Battle {n}: Good triumphs over Evil")
    elif G_score < S_score:
        print(f"Battle {n}: Evil eradicates all trace of Good")
    else:
        print(f"Battle {n}: No victor on this battle field")