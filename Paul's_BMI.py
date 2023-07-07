#bmi.py
import math
choice = input('''
 Select that type of system you want to use for BMI!
1 for imperial
2 for metric
''')


if choice == '1':
    weight = float(input('Please enter your weight in (ibs): '))
    height = float(input('Please enter your height in (in): '))

    h2 = height * height
    w = weight
    BMI = (w / h2) * 703

    print('Your Body Mass Index (BMI) is:', BMI)

    if BMI > 0:
        if BMI < 16:
            print('Severely underweight')
        elif BMI < 17:
            print('Moderately underweight')
        elif BMI < 18.5:
            print('Underweight')
        elif BMI < 25:
            print('Healthy')
        elif BMI < 30:
            print('Overweight')
        elif BMI < 35:
            print('Very Overweight')
        elif BMI <= 40:
            print('Severely Overweight')
        elif BMI > 40:
            print('Extremely Overweight')
    else:
        print('The information that you put in is incorrect.')

if choice == '2':
    h=float(input('Enter your height in meters: '))
    w=float(input('Enter your weight in Kg: '))
    
    BMI=w/(h*h)
    print('BMI Calculated is: ', BMI)
    
    if(BMI<=16):
            print('Very underweight')
    elif(BMI<=18.5):
        print('Underweight')
    elif(BMI<=25):
        print('Healthy')
    elif(BMI<=30):
        print('Overweight')
    else:
        print('Very overweight')

    

    