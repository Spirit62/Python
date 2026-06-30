from abc import ABC, abstractmethod
#Abstraction

class Bank(ABC):
  @abstractmethod
  def deposit(self,amount):
    pass

  @abstractmethod
  def withdraw(self,amount):
    pass

  @abstractmethod
  def show_details(self):
    pass


class savingAccount(Bank):

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


class currentAccount(Bank):
  def __init__ (self,name,initialamount):
    self.name=name;
    self.__initialamount=initialamount;

  def deposit(self,amount):
    self.__initialamount+=amount
    print(f"Your amount of {amount} was deposited succesfully")

  def withdraw (self,amount):
    if amount<=self.__initialamount:

      self.__initialamount-=amount
      print(f"Your amount of {amount} was withdrawn succesfully")
    else:
      print("You do not have sufficient funds")
  def show_details(self):
    print(f"Currently you have Rs. {self.__initialamount} in your bank balance")



print("1.Saving Account\n2. Current Account")
acc_type=int(input("Enter 1 or 2: "))

if acc_type==1:
  account1=savingAccount("Samriddha",10000)
else:
  account1=currentAccount("Samriddha",10000)


print("Welcome to NIMB Bank")

while True:
  print("1. Deposit\n2. Withdraw\n3.Show Details\n4. Exit")
  choice=int(input("Enter your choice"))

  match choice:

    case 1:
        amount = int(input("Enter your amount to deposit: "))
        if amount>0:
          account1.deposit(amount)
        else:
          print("Enter an amount that is positive")

    case 2:
        amount = int(input("Enter your amount to withdraw: "))
        if amount>0 and amount<=100000:
          account1.withdraw(amount)
        else:
          print("Enter a number within 0 and 1 lakh to withdraw")

    case 3:
      account1.show_details()

    case 4:
      print("Thank you for using the app")
      break