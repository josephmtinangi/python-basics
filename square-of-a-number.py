# This program prompt a user to enter a number
# Then the program computes the square of that number
# After computing the square of that number, it determines
# whether the result is greater than 100 or greater than 50 or otherwise

number = int(input('Enter a number.\n'))

numberSquare = number * number

if numberSquare > 100:
    print(numberSquare, ' - Big')
elif 50 < numberSquare < 100:
    print(numberSquare, ' - Medium')
else:
    print('Too small to bother with')
