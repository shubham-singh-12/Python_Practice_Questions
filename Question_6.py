# Write a program to check if a number is prime.

print("\n========== Write a program to check if a number is prime. ==========\n")

def checkPrime():
  number = int(input("Enter number to check it's Prime or Not: "))

  if (number == 0 or number == 1):
    print(f"{number} is not Prime.")

  elif (number > 1):
    for i in range(2, number):
      if (number % i == 0):
        print(f"{number} is not a Prime Number.")
      break

  else:
    print(f"{number} is a Prime Number.")

checkPrime()