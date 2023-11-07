# Simple Calculator
print("Welcome to simple calculator.")
print("I will add/subtract/multiple/divide any two numbers you provide.")
first_input = input("Enter in first number: ")
second_input = input("Enter in second number: ")
operation = input("Would you like to add/subtract/multiple/divide: ")

# explicitly convert string type to float type
first_number = float(first_input)
second_number = float(second_input)
# functions
def add(first_number, second_number):
    return (first_number + second_number)
def subtract(first_number, second_number):
    return (first_number - second_number)
def multiply(first_number, second_number):
    return (first_number*second_number)
def divide(first_number, second_number):
    if second_number!=0:
        return (first_number/second_number)
    else:
        return " Cannot divide by zero! "