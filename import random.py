import random

# List of random phrases
phrases = ["Almost there!", "Try again!", "Nice try!", "Keep going!", "You're close!"]

# The number to guess
number_to_guess = random.randint(1, 100)

while True:
    # Get the player's guess
    guess = int(input("Enter your guess: "))
    
    # Check the guess
    if guess < number_to_guess:
        print("Too low! " + random.choice(phrases))
    elif guess > number_to_guess:
        print("Too high! " + random.choice(phrases))
    else:
        print("You got it! " + random.choice(phrases))
        break
