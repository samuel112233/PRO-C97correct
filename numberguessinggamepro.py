print('Number Guessing Game')
print('Guess a number between 1 and 9')
guess=0
number=3
chances=5
guess=int(input('Enter your guess'))
if(guess==1):
    print('Your guess was too low: Guess a number higher than 1 ')
if(guess==2):
    print('Your guess was too low: Guess a number higher than 2 ')
if(guess==4):
    print('Your guess was too high: Guess a number lower than 4 ')
if(guess==5):
    print('Your guess was too high: Guess a number lower than 5 ')
if(guess==6):
    print('Your guess was too high: Guess a number lower than 6 ')
if(guess==7):
    print('Your guess was too high: Guess a number lower than 7 ')
if(guess==8):
    print('Your guess was too high: Guess a number lower than 8 ')
if(guess==9):
    print('Your guess was too high: Guess a number lower than 9 ')
while chances < 5:
    if guess == number:
        print("CONGRATULATIONS YOU WON!!!")
        break
    else:
        print("YOU LOSE!!! The number is 3")
    chances-=1
print(guess)
print(number)


