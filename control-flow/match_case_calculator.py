#!/usr/bin/env python3
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Choose the operation (+, -, *, /): ").strip()
match operation:
    case "+":
        result = num1 + num2
        print(f"The result is {result:g}.")

    case "-":
        result = num1 - num2
        print(f"The result is {result:g}.")

    case "*":
        result = num1 * num2
        print(f"The result is {result:g}.")

    case "/":
        if num2 == 0:  # or num2 == 0.0 — same thing with float
            print("Cannot divide by zero.")
        else:
            result = num1 / num2
            print(f"The result is {result:g}.")

    case _:  # This is the default case (highly recommended)
        print("Invalid operation selected.")