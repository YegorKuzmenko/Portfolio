num1 = int(input("Enter first number:"))
num2 = int(input("Enter second number:"))

operation = input("Choose operation: + - * / \n")


if operation == "+":
    
    print("Sum is: ", num1 + num2)
    
elif operation == "-":
    print("Minus is: ", num1 - num2)
    
elif operation == "/":
    if num2 != 0:
        print("Div is : ", num1 / num2)
        
    else:
        print("Error, cannot devide 0.")
    
   

else:
    print("Umno is: ", num1 * num2)
    
