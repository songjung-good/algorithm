'''
                        1**0
            1**1                      1**1
        1**2            1**1+1**1         1**2
    1**3    1**2+1**1+1**1  1**1+1**1+1**2  1**3

def fibo1(n):
    global memo
    if n>= 2 and memo[n] == 0:
        memo[n] = fibo1(n-1) + fibo1(n-2)
    return memo[n]

memo = [0] * (n-1)
memo[0] = 0
memo[1] = 1


A**5 A**4+B**1               B
'''
'''
1  2  1
   1  2  1

1 3 3 1
  1 3 3 1

1 4 6 4 1
  1 4 6 4 1   
'''

def triangle(num):
    arr = []
    pre_lst = [0] * num
    point_1 = -1
    point_2 = -1

    for i in range(0, num):
        arr.append([1] * (i+1))
        if i > 1:
            arr.append([0] * i)
            for j in range(i)
                arr[i][j] += arr[i-1][j] + arr[i-1][j]

        pre_lst = arr[i]


    return arr





T = int(input())

for tc in range(1, 1+T):
    N = int(input())
    print(tc, triangle(N))