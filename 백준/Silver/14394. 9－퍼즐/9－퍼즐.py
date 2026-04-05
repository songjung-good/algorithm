def find_w(w):
    c = [0] * 4
    for i in w:
        if i == 'R':
            c[0] += 1
        elif i == 'Y':
            c[1] += 1
        elif i == 'G':
            c[2] += 1
        elif i == 'B':
            c[3] += 1
    
    return c
    
w1 = input()
w2 = input()
c1 = find_w(w1)
c2 = find_w(w2)
ans = 0
for i in range(4):
    ans += abs(c1[i]-c2[i])

print(ans//2)