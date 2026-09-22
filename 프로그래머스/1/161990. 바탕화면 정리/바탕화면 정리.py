def solution(wallpaper):
    min_x, min_y, max_x, max_y = 51, 51, -1, -1
    
    for r in range(len(wallpaper)):
        for c in range(len(wallpaper[0])):
            if wallpaper[r][c] == '#':
                if r < min_x:
                    min_x = r
                if r > max_x:
                    max_x = r
                if c < min_y:
                    min_y = c
                if c > max_y:
                    max_y = c
    answer = [min_x, min_y, max_x+1, max_y+1]
    return answer