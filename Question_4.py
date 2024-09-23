# Write a Python program to find the maximum of two numbers.

print("\n========== Write a Python program to find the maximum of two numbers. ==========\n")

def maximunNumber():
  number_1 = int(input("Enter 1st Number: "))
  number_2 = int(input("Enter 2nd Number: "))

  if number_1 > number_2:
    print(f"\n{number_1} is Greater than {number_2}")
  else:
    print(f"\n{number_2} is Greater than {number_1}")

maximunNumber() 