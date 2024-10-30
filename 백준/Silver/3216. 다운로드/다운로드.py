# N은 노래 조각 수
N = int(input())
music_D = 0
down_V = 0

cnt = 0
for n in range(N):
    D, V = map(int, input().split())
    down_V += V
    # 다운로드 시간이 재생 가능 시간을 초과하면 다운로드 진행
    if music_D < down_V:
        cnt = max(cnt, down_V - music_D)
        down_V -= music_D
        music_D = 0
    else:
        music_D -= down_V
        down_V = 0
    music_D += D

print(cnt)
