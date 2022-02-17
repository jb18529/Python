# MITx 6.00.1x
# Introduction to Computer Science and Programming Using Python
"""
PSET2_3
Calculate minimum monthly payment to pay off balance on credit card.
Input a balance and annual interest rate
Output a fixed monthly rate to two decimal places
Use a bisection search algorithm

"""
balance = 320000
annualInterestRate = 0.2
low = balance/12 #the minimum value is the monthly payments without interest
high = (balance * (1+annualInterestRate)**12)/12.0 #the maximum value is the monthly amount of the balance + interest compounded monthly for an entire year without any payments
while True:
    total = balance
    guess = (high + low)/2.0
    for i in range(1,13):
        total -= guess
        total = total + ((annualInterestRate/12.0) * total)
    #print(total)
    #The total is basically the balance if we used the guess as monthly payments
    #Total does not have to be exact so will allow a range from -0.1 to 0.0
    if total < -0.1:
        high = guess
    elif total > 0.0:
        low = guess
    else:
        break
guess = round(guess, 2)
print("Lowest Payment: " + str(guess))
    


