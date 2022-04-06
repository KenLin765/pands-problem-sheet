## Kenneth Linehan, 2022

## Solution to weekly task 02

##Idea for code from website - https://github.com/mindninjaX/Python-Projects-for-Beginners/blob/master/BMI%20Calculator/BMI%20Calculator.py

height = float(input("Enter height(cm)"))
weight = float(input("Enter weight(kg)"))

##float converts number into number with decimal point

BMI = weight / (height/100)**2

print(f"The BMI is (kg/m2) {BMI}")

##print BMI