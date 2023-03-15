#importing the time module
import time
import random

turns = 10

print("Hello, Let's play hangman! You will have " + str(turns) + " turns!")
print()

# delay
time.sleep(0.5)

# set of words to guess from
wordList = ["javascript", "css", "python", "html"]
word = random.choice(wordList)

guesses = ''

# loop till no turns are remaining
while turns > 0:
    wrong = 0

    for char in word:
        if char in guesses:
            print(char, end=' ')
        else:
            print("_", end=' ')
            wrong += 1

    print("\n")

    if wrong == 0:
        print("You won :)")
        break

    guess = input("Guess a character or enter the correct word: ")[0].lower()
    guesses += guess

    if guess not in word:
        turns -= 1
        print("Wrong")
        print("You have", turns, 'turns left!')

        if turns == 0:
            print("You Lose :(")
