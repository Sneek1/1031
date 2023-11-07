import calculator
print("Welcome to simple calculator.")
print("I will add/subtract/multiple/divide any two numbers you provide.")
first_input = input("Enter in first number: ")
second_input = input("Enter in second number: ")
operation = input("Would you like to add/subtract/multiple/divide: ")

# explicitly convert string type to float type
first_number = float(first_input)
second_number = float(second_input)
# using the functions of calculator
if operation == "add":
    print(calculator.add(first_number, second_number))
if operation == "subtract":
    print(calculator.subtract(first_number, second_number))
if operation == "multiply":
    print(calculator.multiply(first_number, second_number))
if operation == "divide":
    if second_number!=0:
        print(calculator.divide(first_number, second_number))
    else:
        print(" Cannot divide by zero! ")