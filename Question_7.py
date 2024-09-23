# Write a Python program to find the factorial of a number.


# ============================================================================= SOLUTION 1 =============================================================================

print("\n========== Write a Python program to find the factorial of a number. ==========\n")

def factorial():
  number = int(input("Enter number to find Factorial: "))

  if (number == 0 or number == 1):
    result = 1
    print(f"Factorial of {number} is: {result}.")
  elif (number < 0):
    print(f"Factorial of {number} does not Exists.")
  else:
    factorial = 1
    for i in range(1, number + 1):
      factorial *= i
    print(f"Factorial of {number} is: {factorial}")

factorial()


# ============================================================================= SOLUTION 2 =============================================================================

'''import math

def factorial():
  number = int(input("Enter number to find Factorial: "))

  if (number == 0 or number == 1):
    print(f"Factorial of {number} is: 1.")
  elif (number < 0):
    print(f"Factorial of {number} does not exists.")
  else:
    result = math.factorial(number)
    print(f"Factorial of {number} is: {result}")

factorial()'''