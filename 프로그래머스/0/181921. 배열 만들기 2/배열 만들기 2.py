def solution(l, r):
    res = []
    
    from collections import deque
    
    queue = deque(['5'])
    
    while queue:
        num_str = queue.popleft()
        num = int(num_str)
    
        if l <= num <= r:
            res.append(num)

        if num <= r:
            queue.append(num_str + '0')
            queue.append(num_str + '5')
    
    if not res:
        return [-1]
    
    return res