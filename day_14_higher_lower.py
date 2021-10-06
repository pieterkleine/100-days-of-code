from art6 import logo
from art6 import vs
from higher_lower_game_data import data
import random

def get_data(draw):
  name = draw['name']
  description = draw['description']
  country = draw['country']
  extraction = (f"{name}, a {description}, from {country}.")
  return draw['follower_count'], extraction

def compare(answer, first, second):
  if answer == "A":
    return first[0] > second[0]
  elif answer == "B":
    return first[0] < second[0]

print(logo)
score = 0
first = get_data(random.choice(data))
keep_playing = True

while keep_playing:
  second = get_data(random.choice(data))
  print("Compare A: " + first[1])
  print(vs)
  print("Against B: " + second[1])

  while True:
    answer = input("Who has more followers? Type 'A' or 'B': ").upper()
    if answer != "A" and answer != "B":
      print("Invalid entry")
    else:
      break
  
  keep_playing = compare(answer, first, second)
  if keep_playing:
    score += 1
    print(logo)
    print(f"You're right! Current score: {score}")
    first = second
  else:
    print(f"Sorry, that's wrong. Final score: {score}")