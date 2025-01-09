
import random

# Initialize the game
# Step 1: Generate a unique, 4-digit sequence from "0" to "9" without repetition
unique_digits = ''.join(random.sample("0123456789", 4))

# Prepare for the game loop
win = False
attempts = 0

# Game loop
while not win:
    # Step 2: Player makes a guess
    guess = input("Enter your guess (4 unique digits): ")
    
    # Validate the guess
    if len(guess) != 4 or not guess.isdigit() or len(set(guess)) != 4:
        print("Invalid input. Please enter 4 unique digits.")
        continue
    
    attempts += 1
    
    # Step 3 & 4: Compare the guess with the unique sequence and count exact matches (x)
    x = sum(a == b for a, b in zip(unique_digits, guess))
    
    # Step 5: Count partial matches (y)
    y = sum(min(unique_digits.count(g), guess.count(g)) for g in set(guess)) - x
    
    # Step 6: Provide feedback
    print(f"{x}A{y}B")
    
    # Check for winning condition
    if x == 4:
        print(f"Congratulations! You've guessed the sequence in {attempts} attempts.")
        win = True
