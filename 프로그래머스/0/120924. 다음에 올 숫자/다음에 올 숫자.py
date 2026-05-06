def solution(common):
    gap1 = common[-2] - common[-3]
    gap2 = common[-1] - common[-2]
    if gap1 == gap2:
        answer = common[-1] + gap2
    else:
        answer = common[-1] * (common[-1]//common[-2])
    return answer