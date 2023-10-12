
#자릿수 덧셈 문제 

R = int(input())

a = int(R / 1000)
b = int((R % 1000) / 100)
c = int((R % 100) / 10)
d = int(R % 10)
B = int(a+b+c+d)

print(B)
