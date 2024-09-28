A = 0
for i in range(5):
    num = int(input())
    if num < 40:
        num = 40
    A = A + num
    
print(A//5)