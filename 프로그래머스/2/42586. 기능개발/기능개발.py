def solution(progresses, speeds):
    answer = []
    num = len(speeds)
    
    ans = 1
    now = -1
    
    for n in range(num):    
        now_progress = progresses[n]
        now_speed = speeds[n]
        if now_progress < 100:
            now += 1
            answer.append(ans)
            ans = 1
            day = (100 - now_progress) // now_speed
            if now_progress % now_speed:
                day += 1
            for i in range(n+1, num):
                progresses[i] += speeds[i] * day
        else:     
            answer[now] += 1
                
    return answer