N = int(input())
clothes = list(map(int, input().split()))

total_people = sum(clothes)
max_clothes = max(clothes)
if total_people == 1:
    print("Happy")
else:
    if max_clothes > total_people // 2:
        print("Unhappy")
    else:
        print("Happy")
