M, D = map(int, input(). split())
date = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
day = D
if M == 1:
    pass
    # day += D % 7
else:
    for month in range(1, M):
        if month == 2:
            day += 28
        elif month in [4, 6, 9, 11]:
            day += 30
        else:
            day += 31

ans = date[day%7]
print(ans)