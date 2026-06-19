on=True
while on:
  print("Choose a category to convert: ")
  print("1. Length, \n2. Mass, \n3. Time, \n4. Temperature, \n5. Exit")
  choice=int(input("Choice: "))
  if choice<1 or choice>5:
      print("Invalid choice, Enter again!")
      continue
  elif choice==5:
    print("Thank you for using SI unit converter")
    on=False
    continue
  value=float(input("Enter magnitude of your physical quantity: "))
  new_value=None
  if choice==1:
      print("Length conversion")
      print("1. Meter to Kilometer \n2. Kilometer to Meter\n3. Meter to Centimeter\n4. Centimeter to Meter")
      length_choice=int(input("Length_Choice: "))
      if length_choice==1:
        new_value = value/1000
      elif length_choice==2:
        new_value= value*1000
      elif length_choice==3:
        new_value= value*100
      elif length_choice==4:
        new_value = value/100
      else:
        print("Invalid choice, Enter again!")
  elif choice==2:
    print("Mass conversion")
    print("1. Kilogram to gram\n 2. Gram to kilogram")
    mass_choice=int(input("Mass_choice:"))
    if mass_choice==1:
        new_value=value*1000
    elif mass_choice==2:
        new_value=value/1000
    else:
        print("Invalid choice, Enter again!")
  elif choice==3:
    print("Time conversion")
    print("1. Hour to minute\n 2. Minute to hour")
    time_choice=int(input("Time_choice:"))
    if time_choice==1:
        new_value=value*60
    elif time_choice==2:
        new_value=value/60
    else:
        print("Invalid choice, Enter again!")
  elif choice==4:
    print("Temperature conversion")
    print("1. Celsius to Fahrenheit\n 2. Fahrenheit to Celsius")
    temp_choice=int(input("Temp_choice:"))
    if temp_choice==1:
        new_value=(value*9/5)+32
    elif temp_choice==2:
        new_value=(value-32)*5/9
    else:
        print("Invalid choice, Enter again!")
  if new_value is not None:
        print(f"The converted value is {new_value:.2f}")