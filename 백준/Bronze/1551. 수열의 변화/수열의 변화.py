def make_lst(lst):
    num = len(lst)
    new_lst = []
    for n in range(1, num):
        new_lst.append(lst[n] - lst[n-1])
    
    return new_lst
    
N, K = map(int, input().split())
lst=list(map(int, input().split(',')))
for _ in range(K):
    lst = make_lst(lst)

print(*lst, sep=',')
