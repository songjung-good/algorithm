A = [1, 3, 4, 6, 7, 8, 9, 12]
B = [4, 7, 9, 2, 14, 5, 19]

#1
X = len(A)
N = 2               #인덱스 거리 값 수정가능
lst = []            #저장소

for i in range(X//N):    #거리 범위 설정
    lst.append(A[i*N])
ans_1 = sum(lst)
print(ans_1)
print(ans_1//N)

# #2 슬라이싱
# ans = A[0, 8, 1]
#
# print(ans)



#3
N = 3           # 인덱스 거리 N (원하는 값으로 수정)

sum_result = 0  # 저장소
lst_3 = []

for i in range(0, len(A), N): # A[0]부터 인덱스 거리 N마다 원소를 출력하고 더하기
    sum_result += A[i]
    lst_3.append(A[i])

print(sum_result)
avr_3 = sum_result // len(lst_3)
print(avr_3)