'''
1부터 주어진 숫자만큼 모두 더한 값을 출력하시오.

단, 주어질 숫자는 10000을 넘지 않는다.


[예제]

주어진 숫자가 10 일 경우 출력해야 할 정답은,

1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10 = 55
'''






# 1차 통과
num_new = int(input())

num_1 = range(num_new + 1)
num_2 = list(num_1)

print(sum(num_2))

#2차 통과
num_new = int(input())

if num_new >= 1 and num_new <=10000: 
    num_1 = range(num_new + 1)
    num_2 = list(num_1)
    print(sum(num_2))
else:
	pass
