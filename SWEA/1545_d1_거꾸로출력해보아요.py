#1차 오답
num_new = int(input()) 

num_1 = range(num_new, 0, -1)

num_2 = list(num_1)

print(*num_2)





#2차  통과
num_new = int(input()) 

num_1 = range(0, num_new + 1)      #range로 묶임

num_2 = list(num_1)                 #list로 숫자 출력

num_2.reverse()

print(*num_2)                    # *을 통해 언패킹
