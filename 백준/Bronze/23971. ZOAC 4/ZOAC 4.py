H,W,N,M=map(int, input().split())
A=H//(N+1)+1 if H%(N+1) else H//(N+1)
B=W//(M+1)+1 if W%(M+1) else W//(M+1)
print(A*B)