import sys
input = sys.stdin.readline

N = int(input())
songs = [set() for n in range(N+1)]

E = int(input())
song_id = 0

for _ in range(E):
    lst = list(map(int,input().split()))[1:]

    if 1 in lst:
        song_id+=1
        for l in lst:
            songs[l].add(song_id)

    else:
        all_song = set.union(*(songs[l] for l in lst))
        for l in lst:
            songs[l] = all_song.copy()

for i in range(1, N+1):
    if len(songs[i]) == song_id:
        print(i)