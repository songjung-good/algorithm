def check(r, c, m, park):
    for x in range(r, r+m):
        for y in range(c, c+m):
            if park[x][y] != '-1':
                return False
    return True

def solution(mats, park):
    answer = -1
    row, col = len(park), len(park[0])
    mats.sort(reverse=True)
    
    for m in mats:
        if row >= m and col >= m:
            for r in range(row-m+1):
                for c in range(col-m+1):
                    if park[r][c] == '-1':
                        if check(r, c, m, park):
                            return m
                    else:
                        pass
                            
    return answer