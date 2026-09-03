import math

def solution(signals):
    answer = -1
    # 1. 마지막으로 확인할 시간을 먼저 구한다(최소공배수)
    time = [sum(s) for s in signals]
    lcm = time[0]
    
    # 최소공배수 * 최대공약수 = a * b
    for t in time[1:]:
        lcm = t * lcm // math.gcd(t, lcm)
    
    num=len(signals)
    for i in range(1, lcm+1):
        check = True
        # 현재 시간에 노란불인지 확인
        for G, Y, R in signals:
            
            # 해당 시간의 신호등 색
            now = i % (G+Y+R)
            if G < now <= G+Y:
                pass
            else:
                check = False
                break
        if check:
            answer = i
            break
    return answer