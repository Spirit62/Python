class BankAccount:
  def __init__(self,name,account_number):
    self.name=name
    self.account_number=account_number
    self.__balance=1000

  def deposit(self,amount):
    if amount>0:
      self.__balance+=amount
      print(f"Your amount of {amount} was deposited succesfully")
    else:
      print("Please enter a valid amount to deposit")

  def withdraw(self,amount):
    if amount>0 and amount<=self.__balance:
      self.__balance-=amount
      print(f"Your amount of {amount} was withdrawn succesfully")
    else:
      print("You do not have sufficient funds or invalid amount")

  def show_details(self):
    print(f"Hi {self.name} you have Rs. {self.__balance} in your bank balance with account number {self.account_number}")


customers={}

def find_account():
  account= input("Enter Account number: ")
  customer = customers.get(account)

  if customer is None:
    print("Account does not exist!")

  return customer


while True:
  print("1. Create Account\n2. Deposit\n 3. Withdraw\n 4 .show_details\n 5. exit")
  choice=int(input("Enter your choice"))

  match choice:
    case 1:

      account = input("Enter your account number")

      if account in customers:
        print ("Account already exists")
      else:
        name = input("Enter your name")
        customers[account]=BankAccount(name,account)

      print("Account is created sucessfully!")
    case 2:
      customer= find_account()

      if customer:
        amount = float(input("Enter your amount to deposit"))
        customer.deposit(amount)

    case 3:
      customer=find_account()
      if customer:

        amount = int(input("Enter your amount to withdraw"))
        customer.withdraw(amount)

    case 4:
      customer=find_account()
      if customer:
        customer.show_details()

    case 5:
      print("Thank you for using the app")
      break