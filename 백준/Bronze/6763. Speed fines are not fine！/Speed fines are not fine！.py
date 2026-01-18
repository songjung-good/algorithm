limit = int(input())
speed = int(input())
gap = speed - limit
if 1<= gap <= 20:
    print("You are speeding and your fine is $100.")
elif 21 <= gap <= 30:
    print("You are speeding and your fine is $270.")
elif gap >= 31:
    print("You are speeding and your fine is $500.")
else:
    print("Congratulations, you are within the speed limit!")