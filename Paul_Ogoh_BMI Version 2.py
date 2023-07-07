#bmi.py
import math
choice = input('''
 Select that type of system you want to use for BMI!
1 for imperial
2 for metric
''')


if choice == '1':
    heightIN = float(input('Input your height in Inches (in): '))
    weightLB = float(input('Input your weight in Pounds (ibs): '))
    BMI = round(((weightLB/(heightIN*heightIN))*703), 2)
    
    if BMI >= 19 and BMI <= 24:
        print('Your BMI is', BMI, 'Healthy!')
    
    elif BMI >= 25 and BMI <= 29:
        print('Your BMI is', BMI, 'Overweight!')
    
    elif BMI >= 30 and BMI <= 39:
        print('Your BMI is', BMI, 'Very Overweight!')
    
    elif BMI > 39:
        print('Your BMI is', BMI, 'Extremely Overweight!')
    
    elif BMI < 19:
        print('Your BMI is', BMI, 'Underweight!')

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

    

    