'''
같은 학년 같은 성별 만 같은 방

최대 인원 수 K

방의 최소 개수

첫 번째 줄 학생 수를 나타내는 정수 N(1 ≤ N ≤ 1,000)과
최대 인원 수 K(1 < K ≤ 1,000)가 공백으로 분리되어 주어진다.
다음 N 개의 각 줄에는 성별 S와 학년 Y(1 ≤ Y ≤ 6)가 공백으로 분리되어 주어진다.
성별 S는 0, 1중 하나로서 여학생인 경우에 0, 남학생인 경우에 1로 나타낸다.
'''
'''
SY를 좌표로 삼고 숫자를 추가 시키자!
'''

room = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
ans = 0

#N 학생수, K 방 최대 수용인원
N, K = map(int, input().split())
#S 성별, Y 학년
for _ in range(N):
    S, Y = map(int, input().split())
    room[Y][S] += 1

for i in range(1, 7):
    for j in range(2):
        if room[i][j] // K == 0:
            if room[i][j] % K != 0:
                ans += 1
        elif room[i][j] // K != 0:
            if room[i][j] % K != 0:
                ans += (room[i][j] // K) + 1
            else:
                ans += (room[i][j] // K)

print(ans)
