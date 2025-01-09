# Problem 1 Solution

name = input("Enter your name: ")
birthplace = input("Enter your birthplace: ")
hobby = input("Enter your favorite hobby: ")
print(f"I am {name}, I was born in {birthplace}, and my favorite hobby is {hobby}.")

# Problem 2 Solution

num1 = int(input("Enter the first integer: "))
num2 = int(input("Enter the second integer: "))
print(f"Sum: {num1 + num2}")
print(f"Difference: {num1 - num2}")
print(f"Product: {num1 * num2}")
print(f"Average: {(num1 + num2) / 2}")

# Problem 3 Solution

number = float(input("Enter a floating-point number: "))
print(f"Formatted number: {number:.2f}")

# Problem 4 Solution

fahrenheit = float(input("Enter temperature in Fahrenheit: "))
celsius = (fahrenheit - 32) * 5/9
print(f"Temperature in Celsius: {celsius:.2f}")

# Problem 5 Solution

length = float(input("Enter the length: "))
width = float(input("Enter the width: "))
area = length * width
perimeter = 2 * (length + width)
print(f"Area: {area}")
print(f"Perimeter: {perimeter}")

# Problem 6 Solution

initial_investment = float(input("Enter the initial investment amount: "))
monthly_addition = float(input("Enter the monthly addition amount: "))
annual_interest_rate = float(input("Enter the annual interest rate (in percent): ")) / 100
years = int(input("Enter the number of years: "))

total_amount = initial_investment
for i in range(years * 12):
    total_amount += monthly_addition
    total_amount *= (1 + annual_interest_rate / 12)

print(f"Future value of the investment: {total_amount:.2f}")

