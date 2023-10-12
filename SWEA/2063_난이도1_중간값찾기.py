
N = int(input())

if N >= 9 and N <= 199 :
    A = list(map(int, input().split()))
    A.sort()
    index_B=(N+1)//2
    print("{}".format(A[index_B]))

else: pass


