N = int(input())

lst = []

for i in range(1, N+1):
    if str(i) == '3' or str(i) == '6' or str(i) == '9':
        lst.append('-')
        
    elif 10 <= i < 100:
        if str(i)[0] == '3' or str(i)[0] == '6' or str(i)[0] == '9':
            if str(i)[1] == '3' or str(i)[1] == '6' or str(i)[1] == '9':
                lst.append('--')
            elif str(i)[1] != '3' or str(i)[1] != '6' or str(i)[1] != '9':
                lst.append('-')
        else:
            if str(i)[1] == '3' or str(i)[1] == '6' or str(i)[1] == '9':
                lst.append('-')
            elif str(i)[1] != '3' or str(i)[1] != '6' or str(i)[1] != '9':
                lst.append(i)
            
    elif 100 <= i < 1000:
        if str(i)[0] == '3' or str(i)[0] == '6' or str(i)[0] == '9':
            if str(i)[1] == '3' or str(i)[1] == '6' or str(i)[1] == '9':
                if str(i)[2] == '3' or str(i)[2] == '6' or str(i)[2] == '9':
                    lst.append('---')
                else:
                    lst.append('--')
                    
            elif str(i)[1] != '3' or str(i)[1] != '6' or str(i)[1] != '9':
                lst.append('-')
        else:
            if str(i)[1] == '3' or str(i)[1] == '6' or str(i)[1] == '9':
                if str(i)[2] == '3' or str(i)[2] == '6' or str(i)[2] == '9':
                    lst.append('--')
                else:
                    lst.append('-')
            else:
                lst.append(i)
    else:
        lst.append(i)

print(*lst)