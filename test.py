a =int(input("Enter the first number:"))
op = input("Enter the operator:")
b = int(input("Enter the second number:"))


match op :
    case '+':
        print(a+b)
    case '-':
        print(a-b)
    case '%':
        print(a*b)
    case '/':
        if b ==0:
            print("Error: cannot divide by zero")
        else:
            print(a/b)
    case _:
        print("Invalid choice")
        
    
