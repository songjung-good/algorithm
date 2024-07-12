while True:
    A, B = input().split()
    if A == '0' and B == '0':
        break
    else:
        ans = 0
        now = 0
        NUM_A = len(A) - 1
        NUM_B = len(B) - 1
        while NUM_A >= 0 or NUM_B >= 0:
            digitA = int(A[NUM_A]) if NUM_A >= 0 else 0
            digitB = int(B[NUM_B]) if NUM_B >= 0 else 0
            cnt = digitA + digitB + now
            if cnt >= 10:
                ans += 1
                now = 1
            else:
                now = 0
            NUM_A -= 1
            NUM_B -= 1
    print(ans)
