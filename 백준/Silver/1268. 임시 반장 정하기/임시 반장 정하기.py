N = int(input())
MAP = [list(map(int, input().split())) for _ in range(N)]
student = [set() for _ in range(N)]  # 같은 반이었던 학생을 저장할 set 리스트


for j in range(5):  # 1학년부터 5학년까지의 각 학년에 대해
    class_dict = {}

    for i in range(N):  # 각 학생에 대해
        cls = MAP[i][j]
        if cls not in class_dict:
            class_dict[cls] = []
        class_dict[cls].append(i)

    for cls, students in class_dict.items():
        if len(students) > 1:  # 같은 반이었던 학생이 2명 이상인 경우
            for s in students:
                student[s].update(students)  # 서로 같은 반이었던 학생 추가
                student[s].remove(s)  # 자기 자신은 제외

max_count = -1
answer = -1

for i in range(N):
    if len(student[i]) > max_count:  # 가장 많은 친구를 가졌다면 갱신
        max_count = len(student[i])
        answer = i + 1

print(answer)