#from replit import clear
from art import logo
#HINT: You can call clear() to clear the output in the console.

#Dictionary
curent_bids = {}


def greet():
  print(logo)
  print("Welcome to the secret auction program.")

def bidders():
  name = input("What is your name?: ")
  bid = int(input("What is your bid?: $"))
  current_bids[name] = bid
  other_bidders = input("Are there any other bidders? Type 'yes' or 'no'.").lower()
  if other_bidders == 'yes':
    #clear()
    bidders()
  elif other_bidders == 'no':
    max_bid = max(current_bids, key=current_bids.get)
    max_value = current_bids[max_bid]
    print(f"The winner is {max_bid} with a bid of: ${max_value} ")
    

#Koda in hur programmet räknar ut vem som har högsta bud. Det ska sparas i en dictionary.r

greet()
bidders()