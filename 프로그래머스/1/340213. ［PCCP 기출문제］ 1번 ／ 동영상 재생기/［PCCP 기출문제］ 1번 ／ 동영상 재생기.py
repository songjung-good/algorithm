def solution(video_len, pos, op_start, op_end, commands):
    answer = ''
    vid_t = int(video_len[:2]) * 60 + int(video_len[3:])
    pos_t = int(pos[:2]) * 60 + int(pos[3:])
    op_s = int(op_start[:2]) * 60 + int(op_start[3:])
    op_e = int(op_end[:2]) * 60 + int(op_end[3:])
    for c in commands:
        if op_s <= pos_t < op_e:
            pos_t = op_e
        if c == 'next':
            pos_t += 10
            if pos_t > vid_t:
                pos_t = vid_t
        elif c == 'prev':
            pos_t -= 10
            if pos_t < 0:
                pos_t = 0

    if op_s <= pos_t < op_e:
        pos_t = op_e
    
    m = str(pos_t//60).zfill(2)
    s = str(pos_t%60).zfill(2)
    ans = m+':'+s
    return ans