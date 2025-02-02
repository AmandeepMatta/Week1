try:
    num = int(input("Enter any number for factorial: "))
    if num < 0:
        print("Factorial is not defined for negative numbers.")
    else:
        factorial = 1
        for i in range(1, num + 1):
            factorial *= i
        print(f"Factorial of {num} is {factorial}")
except ValueError:
    print("Invalid input. Please enter an integer.")