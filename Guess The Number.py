#function for the guess the number game
from random import randint

num = randint(0,10)
guess = None

def guessnum():
    global guess
    while guess != num:
        guess = input("guess a number between 0 and 10: ")
      
        if guess == ' ':
            print("Please enter a valued number.")
            continue
       
        guess = int(guess)

        if guess == num:
              print("congratulations! you won")
              break
        else:
             print("nope, sorry. try again!")
             
guessnum()

