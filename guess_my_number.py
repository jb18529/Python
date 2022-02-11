# MITx 6.00.1x
# Introduction to Computer Science and Programming Using Python
"""
The program works as follows: you (the user) thinks of an integer between 0 (inclusive) and 100 (not inclusive). 
The computer makes guesses, and you give it input - is its guess too high or too low? 
Using bisection search, the computer will guess the user's secret number!
"""

print("Please think if a number between 0 and 100! ")
low = 0
high = 100
while True:
    guess = (low+high)//2
    q = print("Is your secret number " + str(guess) + "?\n")
    y = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
    if y == 'h':
        high = guess
    elif y == 'l':
        low = guess   
    elif y == 'c':
        break    
    else:
        print("Sorry, I did not understand your input.")
print("Game over. Your secret number was: " + str(guess))    
          
    