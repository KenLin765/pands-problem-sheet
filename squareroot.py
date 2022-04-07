# Kenneth Linehan, 2022
# Program to take a positive floating point number as input and outputs an approximation of its square root

# setting a number for user input and converting to float


# Tutorial which I used for working how to setup the function - https://tutorialspoint.dev/algorithm/algorithms/square-root-of-a-perfect-square
# Returns the square root of n. 
def sqrt(n): 
    # Sqrt function created to square root value
        x = n 
        y = 1
          
        # e decides the accuracy level 
        e = 0.1
        while(x - y > e): 
      
            x = (x + y)/2
            y = n / x 
            # Formula used to calculate square root, manually multiplies number by itself
        return x 
  
n = float(input("Please enter a positive number: "))
# Float is an inbuilt function used to convert a number to string - https://docs.python.org/3/library/functions.html#float

print("Square root of", n, "is", 
              round(sqrt(n), 1)) 
              # Rounds the number to one point
              # Prints the number user gave and the square root of the number
  