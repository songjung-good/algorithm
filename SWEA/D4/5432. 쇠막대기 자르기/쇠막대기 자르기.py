'''
    ( 는 자를 수 있는 파이프를 추가
    ()는 레이저로 자를 수 있는 파이프 만큼 자른 파이프를 추가
    ) 파이프 종료점으로 자를 수 있는 파이프를 하나 줄이고 자른 파이프에 추가
'''

T = int(input())

for tc in range(1, T+1):
    pipe_line = input()

    pipe = 0
    cut_pipe = 0
    for i in range(len(pipe_line)):
        if pipe_line[i] == '(':
            if pipe_line[i+1] == ')':
                cut_pipe += pipe
            else:
                pipe += 1
        else:
            if pipe_line[i-1] == '(':
                pass
            else:
                pipe -= 1
                cut_pipe += 1

    print(f'#{tc} {cut_pipe}')