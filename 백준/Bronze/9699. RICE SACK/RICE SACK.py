포대 = int(input())
for 인덱스 in range(1, 포대+1):
    lst = list(map(int, input().split()))
    print(f'Case #{인덱스}: {max(lst)}')