import math

choice = input('''
SELECT the type of operation you wanna USE!
+ for addition
- for subtraction
* for multiplication
/ for division
** for Exponent
sqrt for Square Root
''')


if choice == '+':
    x = input("Type a number: ")
    y = input("Type another number: ")
    
    sum = int(x) + int(y)
    
    print("The sum is: ", sum)

elif choice == '-':
    first_operand = int(input("Enter the first_operand: "))
    second_operand = int(input("Enter the second_operand: "))
    
    output = first_operand - second_operand
    
    print(output)

elif choice == '*':
    num_1 = int(input('Enter the first number that comes to your mind: '))
    num_2 = int(input('Enter the second number that comes to your mind: '))
    print(' {} * {} = ' .format(num_1,num_2))
    print(num_1 * num_2)

elif choice == '/':
    num_1 = int(input('Enter the first number that comes to your mind: '))
    num_2 = int(input('Enter the second number that comes to your mind: '))
    print(' {} / {} = ' .format(num_1,num_2))
    print(num_1 / num_2)

elif choice == '**':
    num_1 = int(input('Enter the first number that comes to your mind: '))
    num_2 = int(input('Enter the second number that comes to your mind: '))
    print(' {}**{} = ' .format(num_1,num_2))
    print(num_1 ** num_2)

elif choice == 'sqrt':
    num = float(input("Enter a number. "))
    sqRoot = math.pow(num,0.5)
    print("The square root of a given {0} = {1}" .format(num, sqRoot))
    
    

else:
    print('Enter a valid operator, please run the progran again.')
    
