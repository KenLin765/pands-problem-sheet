Problem Set 2022

This contains solutions to a set of different programs.

Please see link to my repository - https://github.com/KenLin765/pands-problem-sheet

Problem 1. Write a program that calculates somebody's Body Mass Index (BMI). Call the file bmi.py The inputs are the person's height in centimetres and weight in kilograms.


Overview of solution

1. Ask user to enter their height in centimetres and weigh in kilograms
2. Create a variable called "BMI" which will store the sum of values of the height and weight
3. We make a function for BMI using this formula (weight / (height/100)**2)
4. We have divided the height by 100 to convert the centimeters into meters.
5. Prints the BMI of the user


Link To Problem - https://github.com/KenLin765/pands-problem-sheet/blob/main/bmi.py


Problem 2. Write a program that asks a user to input a string and outputs every second letter in reverse order.

Example of sentence - The quick brown fox jumps over the lazy dog.

Output of solution - .o zletrv pu o wr cu h

Overview of solution

1. Requests user to enter a sentence, in order to reverse and output every second letter in reverse order

2. The code will then print the sentence with spaces between the word in reverse order


Link- https://github.com/KenLin765/pands-problem-sheet/blob/main/secondstring.py




Problem 3. Write a program that asks the user to input any positive integer and outputs the successive values of the following calculation.

At each step calculate the next value by taking the current value and, if it is even, divide it by two, but if it is odd, multiply it by three and add one.

Have the program end if the current value is one.


### Code Example

$ python collatz.py

Please enter a positive integer: 10

10 5 16 8 4 2 1


Overview of solution

1. Asks user to enter a positive number
2. If user enters a the negative number, it will advise that this won't run and ask user for a positive number again
3. If user enters the number 1, it will ask for a positive number more than 1
4. Outputs the numbers, if even, divided by two, but if it is odd, multiply it by three and add one

Link to file - https://github.com/KenLin765/pands-problem-sheet/blob/main/collatz.py





Problem 4. Write a program that outputs whether or not today is a weekday.


An example of running this program on a Thursday is given below.

$ python weekday.py
Yes, unfortunately today is a weekday.


An example of running it on a Saturday is as follows:

$ python weekday.py
It is the weekend, yay!


Overview of solution

1. The code will import the datetime module in order to confrim the date it is.
2. It will create a variable and record the day in the format eg "Monday"
3. If the day is Monday - Friday, it will advise that today is a weekday
4. If the day is Saturday or Sunday, it will that today is the weekend

Link to file - https://github.com/KenLin765/pands-problem-sheet/blob/main/weekday.py





Problem 5 Write a program that takes a positive floating-point number as input and outputs an approximation of its square root.You should create a function called <tt>sqrt</tt> that does this. This is to demonstrate that you can research and code a process (If you really needed the square root you would use one of the above methods).

Overview of solution

Link to file - https://github.com/KenLin765/pands-problem-sheet/blob/main/squareroot.py

1. Asks user to enter a number, in order to to output a approximation of it's square root
2. Uses inbuilt float function to convert number to floating point number
3. The square root function has been manually created to process the function
4. The code will then report back to the user the number they gave, and the square root of it.




Problem 6 Write a program that reads in a text file and outputs the number of e's it contains. 

Overview of solution -
1. The program will take a document and read the amount of e's located in it.
2. I had both the txt file and program in same folder but file could be adapted to run from a different drive if necessary
3. Program will count the amount of "e" in a file.
4. It will then print the amount of occurences of the letter to the user.


The sample given which I have used is Moby Dick and to calculate the amount of e's in the document

Link to file - https://github.com/KenLin765/pands-problem-sheet/blob/main/countEs.py




Problem 7 - Write a program called plottask.py that displays a plot of the functions f(x)=x, g(x)=x2 and h(x)=x3 in the range [0, 4] on the one set of axes.

Overview of solution -
1. Imports the numpy and matplotlib.pyplot libraries in order to plot the functions
2. Code sets the 3 main functions, for f, g and h in order to plot graph
3. Uses numpy to create an array between 1 and 5.
4. Produces a graph, for the user.

Link to file - https://github.com/KenLin765/pands-problem-sheet/blob/main/plotTask.py


