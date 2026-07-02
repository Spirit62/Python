# def decorator(function):

#   def wrapper():
#     print("Before running a function")

#     function()

#     print ("After running a function")

#   return wrapper


# @decorator
# def greet():
#   print("Hello from greet function")

# greet()


class Calculator:


  @staticmethod
  def add(a,b): #no parameter so no object
    return a+b
  

print(Calculator.add(1,2))
  
