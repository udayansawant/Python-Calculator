# Python Calculator

# List of functions to add, subtract, divide, and multiply two numbers

# Addition
def add(x,y):
    return x + y

# Substraction
def sub(x,y):
    return x - y

# Multiplication
def mul(x,y):
    x * y
    
# Division
def div(x,y):
    x / y
    
    
print("Py-Casio Calculator")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

while True:
    operation = input("Enter the choice/operation: ")
    
    if operation in ('1', '2', '3', '4'):
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
        
        if operation == '1':
            print("Lets perform Addition")
            print(num1, "+", num2, "=", add(num1, num2))
            
        elif operation == '2':
            print("Lets perform Subtraction")
            print(num1, "-", num2, "=", sub(num1, num2))
            
        elif operation == '3':
            print("Lets perform Multiplication")
            print(num1, "*", num2, "=", mul(num1, num2))
            
        elif operation == '4':
            print("Lets perform Division")
            print(num1, "/", num2, "=", div(num1, num2))
            
        
        next_operation = input("Are you up for another operation (yes/no): ")
        if next_operation == 'no' :
            print("See You Again")
            break
            
    
    else:
        print("Invalid Input")