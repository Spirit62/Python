class Banksystem:
  def __init__ (self,name,initialamount):
    self.name=name;
    self.__initialamount=initialamount;

  def deposit(self,amount):
    self.__initialamount+=amount
    print(f"Your amount of {amount} was deposited succesfully")

  def withdraw (self,amount):
    self.__initialamount-=amount
    print(f"Your amount of {amount} was withdrawn succesfully")
  def show_details(self):
    print(f"Currently you have Rs. {self.__initialamount} in your bank balance")



account1=Banksystem("Samriddha",10000)

print("Welcome to NIMB Bank")

while True:
  print("1. Deposit\n 2. Withdraw\n 3.show_details\n 4. exit")
  choice=int(input("Enter your choice"))

  match choice:

    case 1:
      amount = int(input("Enter your amount to deposit"))
      account1.deposit(amount)

    case 2:
      amount = int(input("Enter your amount to withdraw"))
      account1.withdraw(amount)

    case 3:
      pass

    case 4:
      print("Thank you for using the app")

