
import random

from hangman_words import word_list
from hangman_art import stages, logo


# Display the game logo
print(logo)

# Select a random word
chosen_word = random.choice(word_list)

# Calculate the length of the word
word_length = len(chosen_word)

# Create blanks for the chosen word
display = ["_"] * word_length

# Game variables
lives = 6
game_over = False

# Store previously guessed letters
correct_letters = []
guessed_letters = []

# Main game loop
while not game_over:

    print("\n" + " ".join(display))

    print(f"\n******************** {lives}/6 LIVES LEFT ********************")

    # Ask the user to guess a letter
    guess = input("Guess a letter: ").lower().strip()

    # Validate the input
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single alphabet letter.")
        continue

    # Check whether the letter was already guessed
    if guess in guessed_letters:
        print(f"You have already guessed '{guess}'. Try another letter.")
        continue

    # Remember this guess
    guessed_letters.append(guess)

    # Check every letter in the chosen word
    if guess in chosen_word:

        print(f"Good guess! '{guess}' is in the word.")

        correct_letters.append(guess)

        # Reveal all occurrences of the guessed letter
        for position in range(word_length):

            if chosen_word[position] == guess:
                display[position] = guess

    else:

        lives -= 1

        print(
            f"You guessed '{guess}', "
            "that's not in the word. You lose a life."
        )

    # Display the current Hangman stage
    print(stages[lives])

    # Check whether the player has won
    if "_" not in display:

        game_over = True
        print("Congratulations! You win!")

    # Check whether the player has lost
    elif lives == 0:

        game_over = True
        print("You lose!")

# Display the final result
print(f"\nThe correct word was: {chosen_word}")

if lives > 0:
    print("Thanks for playing Hangman!")
 