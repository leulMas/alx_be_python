num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
opp = input("Choose the operation (+, -, *, /): ")

match opp:
    case "+":
        result = num1 + num2
        print(f"The result is {result}")
    case "-":
        result = num1 - num2
        print(f"The result is {result}")
    case "*":
        result = num1 * num2
        print(f"The result is {result}")
    case "/":
        if num2 == 0:
            print("Cannot divide by zero")
        else:
            result = num1 / num2
            print(f"The result is {result}")
    case _:
        print("you have entered a wrong operator")
