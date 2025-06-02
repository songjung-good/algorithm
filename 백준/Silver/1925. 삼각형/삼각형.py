EPS = 1e-8
dot = []
for _ in range(3):
    a, b = map(int, input().split())
    dot.append((a, b))

# 세 점이 일직선 상에 있는지 확인
def check_collinear(p1, p2, p3):
    # 세 점이 일직선 상에 있으면 삼각형을 만들 수 없음
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3
    return abs((x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2))) < EPS

if check_collinear(dot[0], dot[1], dot[2]):
    print('X')
else:
    # 각 변의 길이의 제곱 계산
    line = []
    for i in range(3):
        x1, y1 = dot[i]
        x2, y2 = dot[(i+1)%3]
        line.append((x1 - x2) ** 2 + (y1 - y2) ** 2)

    line.sort()  # 작은 순으로 정렬
    
    # 세 변의 길이가 모두 같으면 정삼각형
    if abs(line[0] - line[1]) < EPS and abs(line[1] - line[2]) < EPS:
        print('JungTriangle')
    # 두 변의 길이가 같으면 이등변삼각형
    elif abs(line[0] - line[1]) < EPS or abs(line[1] - line[2]) < EPS:
        if line[2] > line[0] + line[1]:  # 둔각
            print('Dunkak2Triangle')
        elif abs(line[2] - (line[0] + line[1])) < EPS:  # 직각
            print('Jikkak2Triangle')
        else:  # 예각
            print('Yeahkak2Triangle')
    # 세 변의 길이가 모두 다르면 일반 삼각형
    else:
        if line[2] > line[0] + line[1]:  # 둔각
            print('DunkakTriangle')
        elif abs(line[2] - (line[0] + line[1])) < EPS:  # 직각
            print('JikkakTriangle')
        else:  # 예각
            print('YeahkakTriangle')