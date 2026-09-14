def solution(order):
    answer = 0
    # order: 담아야하는 택배순서, cnt = 택배갯수, main_lst = 컨베이어벨트
    cnt = len(order)
    # A: 메인 컨테이너 벨트_1씩 증가, B: 보조 컨테이너 벨트_1씩 감소
    A, B = order[0], order[0]-1
    
    # # main_lst
    # main_lst = [i for i in range(A, cnt+1)]
    # side_lst = [i for i in range(B, 0, -1)] if B!=0 else []
    
    for o in order:
        if A == o:
            answer += 1
            A += 1
        elif B == o:
            answer += 1
            B -= 1
        else:
            break
    
    return answer