N = int(input())
dict = {}
for _ in range(N):
    title = input().strip()
    if title in dict:
        dict[title] += 1
    else:
        dict[title] = 1

# values를 내림차순으로 정렬하고, values가 같으면 keys를 오름차순으로 정렬
sorted_dict = sorted(dict.items(), key=lambda x: (-x[1], x[0]))

# 가장 첫 번째 요소의 key 출력
print(sorted_dict[0][0])