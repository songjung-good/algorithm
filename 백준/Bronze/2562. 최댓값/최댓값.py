'''
9개의 서로 다른 자연수가 주어질 때, 
이들 중 최댓값을 찾고 그 최댓값이 몇 번째 수인지를 구하는 프로그램을 작성하시오.
'''
max_num = 0
where_max = 0
for i in range(1, 10):
    num = int(input())
    if max_num < num:
        max_num = num
        where_max = i

print(max_num)
print(where_max)
