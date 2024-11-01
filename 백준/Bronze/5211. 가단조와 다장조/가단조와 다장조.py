music = input().split('|')  # 각 마디를 나눔

A_minor_center = {'A', 'D', 'E'}
C_major_center = {'C', 'F', 'G'}
A_cnt, C_cnt = 0, 0

for measure in music:
    first_note = measure[0]
    if first_note in A_minor_center:
        A_cnt += 1
    elif first_note in C_major_center:
        C_cnt += 1

# 판별
if A_cnt > C_cnt:
    print("A-minor")
elif C_cnt > A_cnt:
    print("C-major")
else:
    last_note = music[-1][-1]
    if last_note in A_minor_center:
        print("A-minor")
    else:
        print("C-major")
