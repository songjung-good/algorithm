N,K=input().split()
cnt=0
for h in range(int(N)+1):
    H=str(h)
    for m in range(60):
        M=str(m)
        for s in range(60):
            S=str(s)
            ans=H+M+S
            if len(ans)<6:ans+='0'
            if K in ans:
                cnt+=1
print(cnt)