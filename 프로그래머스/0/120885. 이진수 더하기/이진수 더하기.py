def solution(bin1, bin2):
    def find_digi(bi):
        cnt = len(bi)
        digi = 0
        for i in range(cnt):
            if bi[-1-i] == '1':
                digi += 2 ** (i)
        return digi
    
    digi1, digi2 = find_digi(bin1), find_digi(bin2)
    answer = bin(digi1+digi2)[2:]
        
    return answer