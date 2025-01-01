# 코드를 작성해주세요
while True:
    try:
        word = input()
        while True:
            if 'BUG' in word:
                word = word.replace('BUG', '')
            else:
                print(word)
                break
    except:
        break