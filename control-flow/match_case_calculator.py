num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
opp = input("Choose the operation(+, -, *, /): ")

match opp:
    case "+":
        print(f"The result is {num1 + num2}")
    case "*":
        print(f"The result is {num1 * num2}")
    case "-":
        print(f"The result is {num1 - num2}")
    case "/":
        if num2 == 0:
            print("cannot divide by zero")
        else:
            print(f"The result is {num1 / num2}")
    case _:
        print("you have entered a wrong operator")
