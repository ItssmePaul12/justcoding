if ch == '+':
    print(num1,"+",num2,"=", add(num1,num2))
elif ch == '-':
    print(num1,"-",num2,"=", subtract(num1,num2))
elif ch == '*':
    print(num1,"*",num2,"=", multiply(num1,num2))
elif ch == '/':
    print(num1,"/",num2,"=", divide(num1,num2))
elif ch == '**':
    print(num1, "**", num2, "=", exponent(num1,num2))
elif ch == 'sqrt':
    print(math.sqrt(num1)) 

else:
    print("Error! operator is not correct")