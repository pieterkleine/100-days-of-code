from replit import clear
#HINT: You can call clear() to clear the output in the console.

from art2 import logo
print(logo)

auction = {}

def bid():
  bidder = input("What is your name?: ")
  bid = int(input("What's your bid?: $"))
  auction[bidder] = bid

auction_end = False

while auction_end != True:
  bid()
  audience = input("Are there any more bidders? (y/n): ")
  if audience == "y":
    clear()
  else:
    auction_end = True

highestbid = 0

for person in auction:
  amount = auction[person]
  if amount > highestbid:
    highestbid = amount
    highestbidder = person

print(f"The winner of the action is {highestbidder} with a bid of ${highestbid}.")
