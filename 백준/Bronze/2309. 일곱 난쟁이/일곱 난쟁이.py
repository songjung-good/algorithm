'''
난쟁이 키의 합 100

9명의 난쟁이

난쟁이의 키를 오름차순 정렬
'''
lst = []
for _ in range(9):
    lst.append(int(input()))

total_height = sum(lst)
find_num = total_height - 100

for i in range(9):
    for j in range(9):
        if lst[i]+lst[j] == find_num and i != j:
            lst.pop(j)
            lst.pop(i)
            lst.sort()
            for i in range(7):
                print(lst[i])
        if len(lst) == 7:
            break
    if len(lst) == 7:
        break