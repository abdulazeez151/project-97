import random
print("NumberGuessingGame")
number = random.randlint(1, 9)
chances = 0

while chances < 5:
    
    guess = int(input("Enter Your Guess :- "))

    if guess == number:
        print("Congratulations You Won!!")
        break

    elif guess < number:
        print("Your guess was too low. Guess a higher number than", guess)

    else:
        print("Your guess was too high. Guess a number lower than", guess)

    chances+=1

    if not chances < 5:
        print("You lose!! The number is", number)
        
