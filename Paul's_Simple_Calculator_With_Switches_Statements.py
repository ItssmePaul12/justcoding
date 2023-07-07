import math
print("Welcome to Paul's Calculator with Switches!")
print("Use this calculator for specific purposes. You betta not cheat.")
def calculator(operator, num1, num2):
    match operator:
        case "+":
            return num1 + num2
        case "-":
            return num1 - num2
        case "*":
            return num1 * num2
        case "/":
            return num1 / num2
        case "**":
            return num1 ** num2
        case "sqrt":
            return math.sqrt(num1)
        case __:
            print("Invalid operator!")
            return None
        
operator = input("Enter an operator (+, -, *, /, **, sqrt): ")
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

output = calculator(operator, num1, num2)
if output is not None:
    print("Result:", output)
    
