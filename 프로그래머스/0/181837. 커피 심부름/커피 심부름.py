def solution(order):
    answer = 0
    A = ["iceamericano", "americanoice", "americano", "hotamericano", "americanohot", "anything"]
    B = ["icecafelatte", "cafelatteice", "hotcafelatte", "cafelattehot", "cafelatte"]
    for i in order:
        answer += 4500 if i in A else 5000
        
    return answer