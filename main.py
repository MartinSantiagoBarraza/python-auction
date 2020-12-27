from replit import clear
#HINT: You can call clear() to clear the output in the console.
print("Hello! Welcome to the secret auction")

bids = {}

keep_asking = False

def highest_bids(bids):
  highest_bid = 0
  winner = ""
  for bidder in bids:
    bid_amount = bids[bidder]
    if bid_amount > highest_bid:
      highest_bid = bid_amount
      winner = bidder
  print(f"The winner is {winner} with a bid of ${highest_bid}")

while not keep_asking:
  bidder_name = input("Whats your name?: ")
  bidder_bid = int(input("What's your bid?: $"))
  bids[bidder_name] = bidder_bid
  other_bidder = input("Are there any other bidder? Type 'yes' or 'no': ")
  if other_bidder == 'no':
    keep_asking = True
    highest_bids(bids)
  elif other_bidder == 'yes':
    clear()