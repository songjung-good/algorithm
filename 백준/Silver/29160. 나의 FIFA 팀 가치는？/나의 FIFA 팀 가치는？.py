import sys
import heapq
from collections import defaultdict
input = sys.stdin.readline

N, M = map(int, input().split())
player_dict = defaultdict(list)

# 입력 처리 및 최대 힙 구성
for _ in range(N):
    P, W = map(int, input().split())
    heapq.heappush(player_dict[P], -W)  # 최대 힙을 위해 음수로 저장

ans = 0

# M번의 반복 처리
for i in range(M):
    if i == M - 1:  # 마지막 라운드
        for p in player_dict:
            if player_dict[p]:  # 힙이 비어 있지 않은 경우
                max_value = -heapq.heappop(player_dict[p])  # 최대값 가져오기
                max_value -= 1  # 최대값 감소
                if max_value > 0:
                    heapq.heappush(player_dict[p], -max_value)  # 감소된 값 다시 삽입
                if player_dict[p]:  # 힙이 비어 있지 않으면 최대값 누적
                    ans += -player_dict[p][0]
    else:  # 마지막 라운드가 아닌 경우
        for p in player_dict:
            if player_dict[p]:  # 힙이 비어 있지 않은 경우
                max_value = -heapq.heappop(player_dict[p])  # 최대값 가져오기
                max_value -= 1  # 최대값 감소
                if max_value > 0:
                    heapq.heappush(player_dict[p], -max_value)  # 감소된 값 다시 삽입

print(ans)