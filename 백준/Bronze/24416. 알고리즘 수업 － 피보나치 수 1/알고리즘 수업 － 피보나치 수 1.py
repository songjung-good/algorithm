import sys
input = sys.stdin.readline

'''def fibo1(num):
    if num == 1 or num == 2:
        return 1
    else:
        return fibo1(num - 1) + fibo1(num - 2)'''

def fibo2(num):
    fi = [1] * (num+1)
    for i in range(3, num+1):
        fi[i] = fi[i-1] + fi[i-2]
    return fi[num]

N = int(input())
cnt1 = fibo2(N)
cnt2 = N-2

print(cnt1, cnt2)