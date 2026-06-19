a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a >= b and a >= c:
    print("The greatest number is:", a)
elif b >= a and b >= c:
    print("The greatest number is:", b)
else:
    print("The greatest number is:", c)



# The above program is greatest num, now the below one is Number Guessing Game


secret_number = 42
counter=0
while True:
    
    guess = int(input("Guess the secret number between 1 and 100: "))
    if guess < 1 or guess > 100:
        print("Invalid guess! Please enter a number between 1 and 100.")
        continue

    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
    else:
        print("Congratulations! You guessed the secret number.")
        print("Number of attempts:", counter)
        break