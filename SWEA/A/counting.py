def Counting_Sort(A, B, K):
    #A[] : 입력배열(0 to K)         DATA
    #B[] : 정렬된 배열               TEMP
    #C[] : 카운트 배열(항목별 개수)    COUNTS

    C = [0] * (K+1)       #B말고 C를 넣어야 함

    for i in range(0, len(A)):   #len(A)는 부여됨
        C[A[i]] += 1

    for i in range(1, len(C)):   #
        C[i] += C[i-1]

    for i in range(len(B)-1, -1, -1):
        C[A[i]] -= 1             #count값 하나 감소
        B[C[A[i]]] = A[i]         #count 위치에 배열

