def solution(nums):
    answer = 0
    new_lst = []
    
    for i in nums:
        found = False
        
        for idx, (x, y) in enumerate(new_lst):
            if x == i:
                new_lst[idx] = (x, y + 1)
                found = True
                break
        
        if not found:
            new_lst.append((i, 1))
    
    total = sum(y for x, y in new_lst)
    choice_poke = total / 2
    
    if len(new_lst) >= choice_poke:
        answer = choice_poke
    else:
        answer = len(new_lst)
    
    return answer