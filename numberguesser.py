import random
from turtle import end_fill

n = random.randint(1,10)

print('Welcome to my number guesser game')
print("guess a number between 1 - 10")
num = input ()

#checks that the number is in a relevant range
while (num > 10) or (num<1):
    print("please pick another number")
    num = input ()

while n != num:
    if n<num:
        print('The number is lower than {}. Please guess another number'.format(num))
        num = input ()
    elif n>num:
        print('The number is higher than {}. Please guess another number'.format(num))
        num = input ()

print('You guessed it! The number is {}'.format(n))

