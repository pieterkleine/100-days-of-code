#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪
#HINT 1: https://www.google.com/search?q=how+to+round+number+to+2+decimal+places+python&oq=how+to+round+number+to+2+decimal
#HINT 2: https://www.kite.com/python/answers/how-to-limit-a-float-to-two-decimal-places-in-python

print("Welcome to this tip calculator.")
bill = float(input("How much was the total bill? €"))
people = int(input("Between how many people do you want to split the bill? "))
tip = int(input("How much would you like to tip (%)? "))

result = "{:.2f}".format((bill/people) * (1 + (tip/100)),2)
print(f"Each person should pay €{result}")