import random
from hangman_art import stages, logo
from hangman_words import word_list

lives = 6

# Print LOGO
print(logo)

# Word Choose
chosen_word = random.choice(word_list)
print(chosen_word)

# Word Placeholder
placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print("Word to guess: " + placeholder)

# variables
game_over = False
correct_letters = []

# Game functions
while not game_over:    
  #lives left
    print(f"****************************<{lives}>/6 LIVES LEFT****************************")

  # guess a letter
    guess = input("Guess a letter: ").lower()

    
    if guess in correct_letters:
        print("You've already guessed that letter: " + guess)

  # Curret letters
    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print("Word to guess: " + display)

  # Final Decision after a guess
    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed {guess}, that's not in the word. You lose a life.")

        if lives == 0:
            game_over = True            
            #  word user trying to guess.
            print(f"***********************IT WAS {chosen_word}! YOU LOSE**********************")

    if "_" not in display:
        game_over = True
        print("****************************YOU WIN****************************")

    # Current stages of hangman
    print(stages[lives])
