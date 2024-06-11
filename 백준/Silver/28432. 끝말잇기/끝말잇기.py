def main():
    import sys
    input = sys.stdin.read
    data = input().split()

    N = int(data[0])
    words = data[1:N+1]
    M = int(data[N+1])
    candidates = data[N+2:]

    # 앞뒤 단어와 후보 단어들을 비교하여 올바른 단어를 찾는다.
    for candidate in candidates:
        valid = True

        # 단어 리스트에 후보 단어를 넣어서 중복 체크를 위한 세트
        word_set = set(words)
        word_set.remove('?')
        word_set.add(candidate)

        # 중복 단어가 있으면 유효하지 않다.
        if len(word_set) != N:
            continue

        for i in range(N):
            if words[i] == '?':
                if i > 0 and words[i-1][-1] != candidate[0]:
                    valid = False
                    break
                if i < N-1 and words[i+1] != '?' and candidate[-1] != words[i+1][0]:
                    valid = False
                    break
            else:
                if i > 0 and words[i-1] != '?' and words[i-1][-1] != words[i][0]:
                    valid = False
                    break
                if i < N-1 and words[i+1] != '?' and words[i][-1] != words[i+1][0]:
                    valid = False
                    break
        
        if valid:
            print(candidate)
            break

main()