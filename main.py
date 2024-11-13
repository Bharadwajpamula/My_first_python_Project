import random

print("Welcome to Number guessing Game.")
print("To Win this game, Guess a correct number between 1 to 20 but you will be having only 5 attempts")
attempt=0
max_attempt=5

numbers=random.randint(1,20)
while attempt <= max_attempt:
    try:
        yourGuess=int(input("Enter your guess: "))
        attempt += 1
        
        if not yourGuess.is_integer():
            print("Enter a Valid guess (number)")
            continue
        
        if (yourGuess > numbers):
            print("Lower the number")
        elif (yourGuess < numbers):
            print("Higher the number")
        else:
            print(f"Congratulations! Your Guess is right it's {yourGuess}")
            break
    except ValueError:
        print("Please enter a valid number")

else:
    print(f"Sorry! you have reached maximum attempts. And the answer is {numbers}")