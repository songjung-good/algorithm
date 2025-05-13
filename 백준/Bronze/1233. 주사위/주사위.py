# 코드를 작성해주세요
A, B, C = map(int, input().split())
dict = {}
for a in range(1, A+1):
    for b in range(1, B+1):
        for c in range(1, C+1):
            res = a+b+c
            if res in dict:
                dict[res] += 1
            else:
                dict[res] = 1

sorted_dict = sorted(dict.items(), key=lambda x: x[1], reverse=True)
print(sorted_dict[0][0])