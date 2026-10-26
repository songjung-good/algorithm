def solution(str1, str2):
    answer = 0
    word1 = {}
    word2 = {}
    word_set = set()
    
    # 1번 문자열 집합 원소로 만들기
    for i in range(len(str1)-1):
        now = (str1[i:i+2]).upper()
        # 특수 문자면 빼기
        if now.isalpha():
            if now in word1:
                word1[now] += 1
            else:
                word1[now] = 1
            word_set.add(now)
        
    # 2번 문자열 집합 원소로 만들기 
    for i in range(len(str2)-1):
        now = (str2[i:i+2]).upper()
        # 특수 문자면 빼기
        if now.isalpha():
            if now in word2:
                word2[now] += 1
            else:
                word2[now] = 1
            word_set.add(now)
     
    # 같으면 작은 값을 min, 같으면 큰 값을 max
    # 다르면 max
    max_v = 0
    min_v = 0
    for w in word_set:
        L, R = 0, 0
        if w in word1:
            L = word1[w]
        if w in word2:
            R = word2[w]
        if L > 0 and R > 0:
            min_v += min(L, R)
            max_v += max(L, R)
        else:
            max_v += max(L, R)
    
    if max_v == 0:
        return 65536
    else:
        return int(min_v / max_v * 65536)