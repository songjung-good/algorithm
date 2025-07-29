def solution(schedules, timelogs, startday):
    answer = 0
    workers = len(schedules)
    
    for i in range(workers):
        check = True
        s = schedules[i]
        s_hour = s // 100 * 60
        s_min = s % 100
        date = 0
        for t in timelogs[i]:
            t_hour = t // 100 * 60
            t_min = t % 100
            gap = s_hour + s_min + 10 - (t_hour + t_min)
            if gap < 0 and ((startday+date) % 7) not in [0, 6]:
                check = False
                break
            date += 1
        if check:
            answer += 1
            
    return answer