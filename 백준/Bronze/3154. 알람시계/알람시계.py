import sys
input = sys.stdin.readline

def effort(time):
    dial = [[3, 1], [0, 0], [0, 1], [0, 2], [1, 0], [1, 1], [1, 2], [2, 0], [2, 1], [2, 2]]
    past = None
    cnt = 0
    for t in time:
        now = int(t)
        if past is not None:
            aX, aY = dial[past][0], dial[past][1]
            bX, bY = dial[now][0], dial[now][1]
            cnt += abs(aX - bX) + abs(aY - bY)
        past = now
    return cnt

HH, MM = map(int, input().split(':'))
H_lst = [h for h in range(HH, 100, 24)]
M_lst = [m for m in range(MM, 100, 60)]

min_gap = float('inf')
ans = ''
for h in H_lst:
    h_str = f"{h:02}"  # 두 자리로 변환
    for m in M_lst:
        m_str = f"{m:02}"  # 두 자리로 변환
        time = h_str + m_str
        gap = effort(time)
        if gap < min_gap:
            min_gap = gap
            ans = f"{h_str}:{m_str}"

print(ans)
