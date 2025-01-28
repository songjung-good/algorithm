check = []
for n in range(3):
    word = input()
    if word in ['Fizz', 'FizzBuzz', 'Buzz']:
        pass
    else:
        check = [int(word), 3-n]
        break

now = check[0] + check[1]
if now % 3 == 0 and now % 5 == 0:
    print('FizzBuzz')
elif now % 3 == 0:
    print('Fizz')
elif now % 5 == 0:
    print('Buzz')
else:
    print(now)