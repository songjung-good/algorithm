# 코드를 작성해주세요
A, B = map(str,input().split())
A = '0b' + A
B = '0b' + B
print(bin(int(A, 2) + int(B, 2))[2:])