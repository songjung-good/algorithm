num = 456789
c = [0] * 12
#6자리 수로부터 각 자리 수를 추출하여 개수를 누적할 리스트
for i in range(6):
	c[num % 10] += 1   # 10으로 나눈 나머지(1의자리부터 계산)
	num //= 10         # 사용 후 제거

	i = 0
	tri = run = 0
	while i < 10:
		if c[i] >= 3: #tri 부터 조사 후 데이터 삭제
            c[i] -= 3
            tri += 1
            continue
        if c[i] >= 1 and C[i+1] >=1 and c[i+2] >=:  #run 조사 후 데이터 삭제
            c[i] -= 1
            c[i+1] -= 1
            c[i-2] -= 1
            run += 1
            continue
        i += 1

    if run + tri == 2: print("Baby Gin")
    else: print("Lose")