number = int(input('Enter a number.\n'))

numberSquare = number * number

if numberSquare > 100:
    print(numberSquare, ' - Big')
elif 50 < numberSquare < 100:
    print(numberSquare, ' - Medium')
else:
    print('Too small to bother with')
