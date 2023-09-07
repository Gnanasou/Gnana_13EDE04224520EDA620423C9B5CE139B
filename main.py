# 1.1 Implement a recursive function to calculate the factorial of a given number.


def factorial(n):
  if n == 0:
    return 1
  else:
    return n * factorial(n - 1)


# Get user input for the number
number = int(input("Enter a number to calculate its factorial: "))

# Calculate the factorial
result = factorial(number)

# Display the result
print("The factorial of {} is {}.".format(number, result))
