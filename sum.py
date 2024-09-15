def sum(num1, num2):
    return num1 + num2

try:
    number1 = float(input("Enter the first number: "))
    number2 = float(input("Enter the second number: "))
except ValueError:
    print("Please only enter numeric values.")
    exit()

res = sum(number1, number2)

print(f"The sum of {number1} and {number2} is {res}.")
