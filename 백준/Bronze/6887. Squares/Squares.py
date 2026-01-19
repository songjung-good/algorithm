# 코드를 작성해주세요
N=int(input())
ans = 0
for i in range(1, 101):
    if i**2 > N:
        break
    else:
        ans = i
print(f"The largest square has side length {ans}.")