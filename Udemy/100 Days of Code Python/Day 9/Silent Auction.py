import os
from SilentArt import logo
bidders = []

def new_bidder(name, bid):
    new_bid = {}
    new_bid['name'] = name
    new_bid['bid'] = bid
    bidders.append(new_bid)
    

auction = False

while not auction:
    print(logo)
    name = input('What is your name?\n ')
    amount = int(input('What is the amount you would like to bid?\n '))
    new_bidder(name, amount)
    others = input('Are there any other bidders? Type "yes" or "no".\n ').lower()
    print(others)
    if others == 'yes':
        os.system('cls')
    elif others == 'no':
        os.system('cls')
        auction = True

highest_bid = {'bid': 0}
for bid in bidders:
    if bid['bid'] < highest_bid['bid']:
        print(f"Sorry but {bid['name']} did not win the auction with a bid of {bid['bid']}")
    elif bid['bid'] > highest_bid['bid']:
        highest_bid = bid

print(f"{highest_bid['name']} won the auction with a bid of {highest_bid['bid']}")
