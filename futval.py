#   futval.py
#   A program to compute the value of an investment
#   carried 10 years into the future
#   by Paul Ogoh, June 13, 2023

def main():
    print("This program calculates the future value of a 10-year investment.")

    principal = eval(input("Enter the initial principal:"))
    apr = eval(input("Enter the annual interest rate:"))
    year = eval(input("Enter your years"))
    
    for i in range(year):
        principal = principal * (1 + apr)
    print("The value in 10 years is:", principal)

main()

