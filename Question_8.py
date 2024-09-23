# Write a Python program to find the sum of digits of a number.

print("\n========== Write a Python program to find the sum of digits of a number. ==========\n")

def sumOfDigit():
  
  # USER INPUT
  number = (input("Enter Number to find it's Sum: "))

  sum = 0
  for i in range(number):
    sum += int(i)
  print(f"Sum of {number} is {sum}")

sumOfDigit()