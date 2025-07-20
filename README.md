import random

# List of words for the game
words = ["python", "hangman", "challenge", "program", "developer"]

# Randomly choose a word
secret_word = random.choice(words)
guessed_letters = []  # List to store guessed letters
tries = 6  # Number of tries allowed

print("Welcome to Hangman!")
print("_ " * len(secret_word))  # Print blanks

# Main game loop
while tries > 0:
    guess = input("Guess a letter: ").lower()

    if not guess.isalpha() or len(guess) != 1:
        print("Please enter a single letter.")
        continue

    if guess in guessed_letters:
        print("You've already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in secret_word:
        print("Good guess!")
    else:
        print("Wrong guess!")
        tries -= 1

    # Display current state of the word
    display_word = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display_word# stock-portfolio-tracker
automate a small,real life repetitive task
