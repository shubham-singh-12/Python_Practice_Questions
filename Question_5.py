# Write a Python program to check whether a number is even or odd.

print("\n========== Write a Python program to check whether a number is even or odd. ==========\n")

def checkEvenOdd():
  number = int(input("Enter number to check Even / Odd: "))

  if (number % 2 == 0):
    print(f"{number} is Even.")
  else:
    print(f"{number} is Odd.")
  
checkEvenOdd()