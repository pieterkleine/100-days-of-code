#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

def compare(guess, number):
  """Compares a guessed number to the number to be guessed and returns a boolean to designate whether the player wins or not"""
  if guess > number:
    print("Your guess was too high.")
    return True
  elif guess < number:
    print("Your guess was too low.")
    return True
  else:
    print("You got it!")
    return False

from art5 import logo
import random
print(logo)

print("Welcome to this number guessing game.")
print("I'm thinking of a number between 1 and 100.")

number = random.randint(1,100)
not_guessed = True

while True:
  difficulty = input("Choose a difficulty, 'easy' or 'hard': ").lower()
  if difficulty == 'easy' or difficulty == 'hard':
    break
  else:
    print("Invalid difficulty.")

if difficulty == 'easy':
  guesses_left = 10
else:
  guesses_left = 5

while not_guessed and guesses_left > 0:
  print(f"You have {guesses_left} guess remaining.")
  guess = int(input("Make a guess: "))
  not_guessed = compare(guess, number)
  guesses_left -= 1

  if guesses_left == 0:
    print(f"The number I had in mind was {number}.")