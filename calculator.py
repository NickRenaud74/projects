import math


def calculate():
    def add(x, y):
        return x + y

    def subtract(x, y):
        return x - y

    def multiply(x, y):
        return x * y

    def divide(x, y):
        try:
            return x / y
        except ZeroDivisionError:
            return "Cannot divide by Zero"

    def power(x, y):
        return x ** y

    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Power")

    try:
        choice = (input("Enter choice(1, 2, 3, 4, 5): "))
        if choice not in ["1", "2", "3", "4", "5"]:
            print("Invalid input")
            print()
            calculate()

        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

    except ValueError:
        print("Please only enter numbers")
        print()
        again()

    if choice == "1":
        print(num1, "+", num2, "=", add(num1, num2))
    elif choice == "2":
        print(num1, "-", num2, "=", subtract(num1, num2))
    elif choice == "3":
        print(num1, "*", num2, "=", multiply(num1, num2))
    elif choice == "4":
        print(num1, "/", num2, "=", divide(num1, num2))
    elif choice == "5":
        print(num1, "**", num2, "=", power(num1, num2))
    else:
        print("invalid input")

    print()
    again()


def again():
    calc_more = input("Do you want to continue using calculator? Please type Y for yes, N for no. ")
    if calc_more.upper() == "Y":
        calculate()
    elif calc_more.upper() == "N":
        print("Have a good day!")
    else:
        print()
        again()


def welcome():
    print("Welcome to calculator!")
    print()


if __name__ == "__main__":
    welcome()
    calculate()
