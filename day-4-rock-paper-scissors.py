rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

import random

player = input("Choose rock, paper or scissors: ")
computer = random.choice([rock, paper, scissors])

if player.lower() == "rock":
  print(rock)
  if computer == rock:
    result = "A tie!"
  elif computer == paper:
    result = "You lose!"
  else:
    result = "You win!"
elif player.lower() == "paper":
  print(paper)
  if computer == rock:
    result = "You win!"
  elif computer == paper:
    result = "A tie!"
  else:
    result = "You lose!"
else:
  print(scissors)
  if computer == rock:
    result = "You lose!"
  elif computer == paper:
    result = "You win!"
  else:
    result = "A tie!"

print("\nComputer chose:\n" + computer)
print(result)