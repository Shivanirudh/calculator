import sys
import math

def square_root(x):
    """Function to calculate the square root of a number"""
    return math.sqrt(x)

def factorial(x):
    """Function to calculate the factorial of a number"""
    return math.factorial(x)

def natural_logarithm(x):
    """Function to calculate the natural logarithm of a number"""
    return math.log(x)

def power(x, y):
    """Function to calculate the power of a number"""
    return x ** y

def main():
    if len(sys.argv) < 3:
        print("Usage: python3 app.py <operation> <operand1> [operand2]")
        print("<operation>: sqrt, fact, ln, pow")
        return

    operation = sys.argv[1]
    operand1 = float(sys.argv[2])

    if operation == 'sqrt':
        print("Result:", square_root(operand1))
    elif operation == 'fact':
        print("Result:", factorial(int(operand1)))
    elif operation == 'ln':
        print("Result:", natural_logarithm(operand1))
    elif operation == 'pow':
        if len(sys.argv) != 4:
            print("Usage: python3 app.py pow <base> <exponent>")
            return
        operand2 = float(sys.argv[3])
        print("Result:", power(operand1, operand2))
    else:
        print("Invalid operation. Please choose from sqrt, fact, ln, pow")

if __name__ == "__main__":
    main()

