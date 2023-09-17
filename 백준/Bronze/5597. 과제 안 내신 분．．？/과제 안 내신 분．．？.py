'''
1 ~ 30번 학생
28명 제출 (각 줄 마다 있음)
제출 안한 번호 출력
'''
student_num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18 ,19,20, 21,22 ,23, 24, 25, 26, 27, 28, 29, 30]
for i in range(28):
    summit_student = int(input())
    student_num.remove(summit_student)

student_num.sort(reverse=True)
print(student_num.pop())
print(student_num.pop())