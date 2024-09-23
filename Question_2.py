# Write a program to add two numbers.

print("\n========== Write a program to add two numbers. ==========\n")

def addNumbers():
  number_1 = int(input("Enter 1st Number: "))
  number_2 = int(input("Enter 2nd Number: "))
  sum = number_1 + number_2
  print(f"Sum of {number_1} & {number_2} is: {sum}")

addNumbers()