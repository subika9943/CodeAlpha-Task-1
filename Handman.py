import random

words = ["apple", "banana", "grapes", "orange", "mango"]
word = random.choice(words)

guessed = []
tries = 6

print("Welcome to Hangman")

while tries > 0:
    display = ""
    for ch in word:
        if ch in guessed:
            display += ch
        else:
            display += "_"

    print(display)
    print("Tries left:", tries)

    if "_" not in display:
        print("You won!")
        break

    letter = input("Enter a letter: ")

    if letter in guessed:
        print("Already guessed")
        continue

    guessed.append(letter)

    if letter not in word:
        tries -= 1
        print("Wrong guess")

if tries == 0:
    print("Game Over! Word was:", word)
