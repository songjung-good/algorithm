# 코드를 작성해주세요
A = int(input())
B = int(input())
for i in range(A, B+1):
    if i == A:
        print(f"All positions change in year {i}")
    else:
        if (i - A) % 60 == 0:
            print(f"All positions change in year {i}")
        