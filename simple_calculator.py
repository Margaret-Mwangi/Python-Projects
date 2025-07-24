while True:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    print("Operations")
    print("1.Add")
    print("2.Subtract")
    print("3.Multiply")
    print("4.Divide")

    operation = int(input("Select the operation (1/2/3/4): "))

    if operation == 1:
        result = num1 + num2
        print(f"{num1} + {num2} ={result}")
    elif operation == 2:
        result = num1 - num2
        print(f"{num1} - {num2} ={result}")
    elif operation == 3:
        result = num1 * num2
        print(f"{num1} * {num2} ={result}")
    elif operation == 4:
        if num2 == 0:
            print("Error, division by 0")
        else:
            result = num1 / num2
            print(f"{num1} / {num2} = {result}")
    else:
        print("Invalid Operation")
    
    more_calculations = input("Would you like to do another calculation?(y/n): ")

    if more_calculations == "y":
        continue
    else:
        break