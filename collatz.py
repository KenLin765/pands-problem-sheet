#Kenneth Linehan, 2022

#Write a program that asks the user to input any positive integer and outputs the successive values of the following calculation.

#At each step calculate the next value by taking the current value and, if it is even, divide it by two, but if it is odd, multiply it by three and add one.

#Source used to help with code - https://stackoverflow.com/questions/33508034/making-a-collatz-program-automate-the-boring-stuff

def collatz(number):   ##Code used to define function
    if number % 2 == 0: ## modulo operator, it divides the first by the second and returns the remainder
        return number // 2 ## // used to get division result
    elif number % 2 == 1:
        return 3 * number + 1 ## this outputs the successive value
## https://docs.python.org/3.3/library/stdtypes.html#printf-style-string-formatting - Researched in order to figure out how % works


try:
    chosenInt = int(input('Please enter a positive integer: ')) ## Asks user to enter a number

    while chosenInt < 2: # Potential error code, if someone picks incorrect number
        print("Number is too small. Please input a positive integer, more than 2: ")
        chosenInt = int(input('Ensure number is greater than 1 '))

    print(chosenInt)

    while chosenInt != 1:   ##
        chosenInt = collatz(chosenInt)
        print(chosenInt)

except ValueError:  ##ValueError is a built in function - https://docs.python.org/3/library/exceptions.html
    ## Raised when an operation or function receives an argument that has the right type but an inappropriate value
    
    print('Sorry, you must enter an integer.')

    ## Indicates the user has entered something incorrect