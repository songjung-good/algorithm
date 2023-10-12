A = [1, 3, 4, 6, 7, 8, 9, 12]
B = [4, 7, 9, 2, 14, 5, 19]

#1



#2
ans = A[0, 8, 1]

print(ans)


#3
N = 3  # 인덱스 거리 N (원하는 값으로 수정)

sum_result = 0  # 덧셈 결과를 저장할 변수 초기화

for i in range(0, len(A), N): # A[0]부터 인덱스 거리 N마다 원소를 출력하고 더하기
    print(A[i])
    sum_result += A[i]

print("덧셈 결과:", sum_result)