
on = True
while on:
  print ("1, Addition \n2, Subtraction \n3, Division \n4, Multiplication \n5, Exit")

  print("Enter any number from 1 to 5 ")
  choice = int(input("Choice: "))
  if choice<1 or choice>8:
      print("Invalid choice, Enter again!")
      continue
  if choice ==5:
      print("Thank you for using calculator")
      break

  num1 = float(input("Enter first number "))
  num2 = float(input("Enter second number "))
  if choice == 1:
      result = num1 + num2
      print(f"The sum of {num1} and {num2} is {result}")
  elif choice == 2:
      result = num1 - num2
      print(f"The subtraction of {num1} and {num2} is {result}")
  elif choice == 3:
      result = num1 / num2
      print(f"The division of {num1} and {num2} is {result}")
  elif choice == 4:
      result = num1 * num2
      print(f"The multiplication of {num1} and {num2} is {result}")
  else:
      print("Enter a valid number from 1 - 5")

  print("/n hello")