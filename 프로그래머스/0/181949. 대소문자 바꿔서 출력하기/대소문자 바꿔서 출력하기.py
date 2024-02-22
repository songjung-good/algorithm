str = input()
num = len(str)
word = ""
for i in range(num):
    nowword=str[i]
    if nowword.isupper() is True:
        nowword = nowword.lower()
        word = word + nowword
        
    else:
        nowword = nowword.upper()
        word = word + nowword
print(word)