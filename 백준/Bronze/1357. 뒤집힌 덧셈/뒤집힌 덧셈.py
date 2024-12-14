# 코드를 작성해주세요
X, Y = map(str, input().split())
new_X = ''
new_Y = ''
for x in X:
    new_X = x + new_X
for y in Y:
    new_Y = y + new_Y

Z = str(int(new_X) + int(new_Y))

new_Z = ''
for z in Z:
    new_Z = z + new_Z

print(int(new_Z))