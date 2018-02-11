# Guess the number game
import random # import 'random'
# Spacing
guesses_taken = 0 # set a variable for guesses taken
# Another spacing
print('Hello! What is your name?') # prints initial message
myName = input() # takes a user input an sets is as variable
# Yet another spacing
number = random.randint(1, 20) # takes a random number between 1 and 20
print('Well, ' + myName + ', I am thinking of a number between 1 and 20.') # prints a message
# Look @ line 3 for reference
while guesses_taken < 6: # loops while variable is lower than 6
    print('Take a guess.')  # another message
    guess = input() # takes user input and sets it as variable
    guess = int(guess) # changes variable type to integer
# Guess what?
    guesses_taken += 1 # increases value of the variable by 1
# Fortunately this code isn't too long
    if guess < number:  # checks if user input is lower than random number
        print('Your guess is too low.') # prints a message
# Is it...?
    if guess > number: # checks if user input is higher than random number
        print('Your guess is too high.') # prints a message
# I think i can see the end
    if guess == number: # checks if user input is equal to random number
        break # breaks the loop
# Almost there!
if guess == number: # checks if user input is equal to random number
    guesses_taken = str(guesses_taken) # converts the variable to string
    print('Good job, ' + myName + '! You guessed my number in ' + guesses_taken + ' guesses!') # prints a victory message with user name and amount of guesses taken
# YES!
if guess != number: # checks if user input is different from random number
    number = str(number) # converts the variable to string
    print('Nope. The number I was thinking of was ' + number) # prints a loss message with the random number
