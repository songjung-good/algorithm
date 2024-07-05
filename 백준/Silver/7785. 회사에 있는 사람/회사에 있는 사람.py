CNT = int(input())
SET = set([])
for i in range(CNT):
    NAME, STATE = map(str, input().split())
    if STATE == 'enter':
        SET.add(NAME)
    else:
        SET.remove(NAME)
        
LIST = list(SET)
LIST.sort(reverse=True)
for j in LIST:
    print(j)