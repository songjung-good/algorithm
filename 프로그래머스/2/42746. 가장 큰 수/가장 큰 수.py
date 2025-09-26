from functools import cmp_to_key
def com(x, y):
    if x + y > y + x:
        return -1
    elif x + y < y + x:
        return 1
    else:
        return 0

def solution(numbers):

    num_lst = list(map(str, numbers))
    num_lst.sort(key=cmp_to_key(com))
    ans = ''
    for i in num_lst:
        ans += i
    if int(ans) == 0:
        return '0'
    return ans