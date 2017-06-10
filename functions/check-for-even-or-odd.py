# Check whether a number is even or odd

def check(number):

    if number % 2 == 0:
        print('Even')
    else:
        print('Odd')


number = int(input('Enter a number\n'))

check(number)
