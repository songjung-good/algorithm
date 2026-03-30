# 코드를 작성해주세요
w = float(input())
h = float(input())
h = h**2
bmi = w/h
if bmi > 25:
    print('Overweight')
elif bmi < 18.5:
    print('Underweight')
else:
    print('Normal weight')