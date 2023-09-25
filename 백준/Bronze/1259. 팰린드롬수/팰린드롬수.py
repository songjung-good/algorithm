while True:
    A = input()
    word_lng = len(A)
    if A == '0':
        break
    else:
        if word_lng == 1:
            print('yes')
        elif word_lng % 2 == 1:
            if A[:word_lng//2] == A[word_lng:word_lng//2:-1]:
                print('yes')
            else:
                print('no')
        else:
            if A[:word_lng//2] == A[word_lng:word_lng//2-1:-1]:
                print('yes')
            else:
                print('no')