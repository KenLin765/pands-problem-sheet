# Kenneth Linehan, 2022
# Program to take a positive floating point number as input and outputs an approximation of its square root

# setting a number for user input and converting to float
n = float(input("Please enter a positive number: "))

## I used this source to figure out start of the issue - https://python.pages.doc.ic.ac.uk/2021/lessons/lesson04/05-break/06-newtonsolution.html
#guess is used to hold the number
guess = n
epsilon = 0.01

#epsilon ensures that a positive number is entered

while True:
    old_guess = guess
    guess = (guess + n/guess) * 0.5
    if abs(guess - old_guess) < epsilon:
        print("The square root of ",n," is approx.",guess,)
        ##print the answer
        break
