#Day 9 Project - dictionaries and nesting
clear()
auction_bids = {}

logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
print(logo)
name = input("Enter your name :")
bid = int(input("Enter your bid amount: $"))
auction_bids[name]=bid
more_bidders = "yes" == input("Enter 'yes' if there are more bidders: ")

while more_bidders:
    clear()

    name = input("Enter your name :")
    bid = int(input("Enter your bid amount: $"))
    auction_bids[name]=bid
    more_bidders = "yes" == input("Enter 'yes' if there are more bidders: ")

winner_bid = list(auction_bids.values())[0]
winner_name = list(auction_bids.keys())[0]

for name in auction_bids.keys():
    if auction_bids[name] > winner_bid:
        winner_name = name
        winner_bid = auction_bids[name]

clear()
print(auction_bids)
print(f"The winner is {winner_name} with a bid of ${winner_bid}")
