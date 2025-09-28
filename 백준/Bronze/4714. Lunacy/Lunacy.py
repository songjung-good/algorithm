# 코드를 작성해주세요
while True:
    num = float(input())
    if num == -1.0:
        break
    else:
        earth = "{:.2f}".format(num)
        moon = "{:.2f}".format(num * 0.167)        
        print(f'Objects weighing {earth} on Earth will weigh {moon} on the moon.')