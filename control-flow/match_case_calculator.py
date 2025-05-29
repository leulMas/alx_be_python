num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
opp = input("Choose the operation (+, -, *, /): ")

match opp:
    case "+":
        result = num1 + num2
        print("The result is", [result])
    case "*":
        result = num1 * num2
        print("The result is", [result] )
    case "-":
        result = num1 - num2
        print("The result is", [result] )
    case "/":
        if num2 == 0:
            print("cannot divide by zero5")
        else:
            result = num1 / num2
            print("The result is", [result])
    case _:
        print("you have entered a wrong operator")
