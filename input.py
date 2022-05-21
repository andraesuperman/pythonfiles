x = int (input("number 1: "))
y = int (input("number 2: "))
operator = input("1 - Addition\n2 - Subtraction\n3 - Multiplication\n4 - Division\nChoose: ")
if(operator == '1'):
    sum = x + y
    print(sum)
elif (operator == '2'):
    difference = x - y
    print (difference)  
elif (operator == '3'):
    product = x * y
    print(product)
elif (operator == '4'):
    quotient = x / y
    print(quotient)
else:
    print("That's not part of the choices")
