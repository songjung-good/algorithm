N,K=input().split()
X=0
for h in range(int(N)+1):
    for m in range(60):
        for s in range(60):
            Y=str(h)+str(m)+str(s)
            if len(Y)<6:Y+='0'
            if K in Y:
                X+=1
print(X)