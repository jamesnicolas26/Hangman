import random

words = ['python', 'jave', 'kotlin', 'javascript']
chosen_word = random.choice(words)
guessed_word = ['_'] * len(chosen_word)
attempts = 6
guessed_letters = set()

def display():
    print(" ".join(guessed_word))
    print(f"Attempts: {attempts}")

while attempts > 0 and '_' in guessed_word:
    display()
    guess = input("Guess a letter: ").lower()

    if guess in guessed_letters:
        print(f"You have already guessed that letter.")
    elif guess in chosen_word:
        for index, letter in enumerate(chosen_word):
            if letter == guess:
                guessed_word[index] = guess
    else:
        attempts -= 1
        print("Incorrect guess.")

    guessed_letters.add(guess)

if '_' not in guessed_word:
    print("Congratulations! You guessed the word:", chosen_word)
else:
    print("Sorry, you ran out of guesses. The word was:", chosen_word)