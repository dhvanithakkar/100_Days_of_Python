logo = """
88          88                       88        88                       88
88          88                       88        ""                       88
88          88                       88                                 88
88,dPPYba,  88 ,adPPYYba,  ,adPPYba, 88   ,d8  88 ,adPPYYba,  ,adPPYba, 88   ,d8
88P'    "8a 88 ""     `Y8 a8"     "" 88 ,a8"   88 ""     `Y8 a8"     "" 88 ,a8"
88       d8 88 ,adPPPPP88 8b         8888[     88 ,adPPPPP88 8b         8888[
88b,   ,a8" 88 88,    ,88 "8a,   ,aa 88`"Yba,  88 88,    ,88 "8a,   ,aa 88`"Yba,
8Y"Ybbd8"'  88 `"8bbdP"Y8  `"Ybbd8"' 88   `Y8a 88 `"8bbdP"Y8  `"Ybbd8"' 88   `Y8a
                                              ,88
                                            888P"
"""
def ace_to_1(cards):
    if sum(cards)> 21 and 11 in cards:
        cards.remove(11)
        cards.append(1)
    return cards

def hit(cards, person):
    cards = cards + [random.choice(all_cards)]
    cards = ace_to_1(cards)
    print(f"{sum(cards)}\t{person} Cards are: \t{cards}")
    return cards

def stand(player_cards, dealer_cards, bet_placed, money_in_bank):
    print(f"{sum(dealer_cards)}\tDealer's Cards are: \t{dealer_cards}")

    while sum(dealer_cards) < 17:
        print("Dealer has less than 17 score.\n")
        dealer_cards = hit(dealer_cards, "Dealer's")

    print(f"{sum(player_cards)}\tYour Cards are: \t{player_cards}")
    return winner(player_cards, dealer_cards, bet_placed, money_in_bank)

def winner(player_cards, dealer_cards, bet_placed, money_in_bank):
    if sum(dealer_cards) > 21:
            print(f"Bust. You Win!!")
            return money_in_bank + 2*bet_placed
    elif sum(player_cards) > 21:
        print(f"Bust. You Lose.")
        return money_in_bank

    elif sum(player_cards) > sum(dealer_cards):
        print("You Win!!")
        return money_in_bank + 2*bet_placed
    elif sum(player_cards) < sum(dealer_cards):
        print("You Lose.")
        return money_in_bank
    else:
        print("Draw.")
        return money_in_bank + bet_placed

def hit_or_stand(choice, player_cards, dealer_cards, bet_placed, money_in_bank):
    player_cards = ace_to_1(player_cards)
    dealer_cards = ace_to_1(dealer_cards)
    
    while choice not in ['hit', 'stand']:
        choice = input("Invalid Choice. Enter whether to Hit or Stand: ").lower()
        return hit_or_stand(choice, player_cards, dealer_cards, bet_placed, money_in_bank)

    if sum(player_cards) == 21:
            print(f"Blackjack. You Win!!!")
            return money_in_bank + 2*bet_placed

    if choice == 'hit':
        player_cards = hit(player_cards, "Your")
        if sum(player_cards) > 21:
            print(f"Bust. You Lose.")
            return money_in_bank

        elif sum(player_cards) == 21:
            print(f"Blackjack. You Win!!!")
            return money_in_bank + 2*bet_placed

        choice = input("\nEnter whether to Hit or Stand: ").lower()
        return hit_or_stand(choice, player_cards, dealer_cards, bet_placed, money_in_bank)

    else:
        return stand(player_cards, dealer_cards, bet_placed, money_in_bank)
    
import random
all_cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
from IPython.display import clear_output

def play_blackjack(money_in_bank):
    clear_output()
    print(logo)
    print(f"\nYou have: ${money_in_bank}")
    bet_placed = int(input("Enter betting amount: $"))
    while bet_placed > money_in_bank:
        bet_placed = int(input("Insufficient money in the Bank. Enter new bet: "))
    money_in_bank -= bet_placed
    player_cards = ace_to_1([random.choice(all_cards) for _ in range(2)])
    dealer_cards = ace_to_1([random.choice(all_cards) for _ in range(2)])

    print(f"\n{dealer_cards[0]}\tDealer's visible card is: \t{dealer_cards[0]}")
    print(f"{sum(player_cards)}\tYour cards are:           \t{player_cards}")

    choice = input("\nEnter whether to Hit or Stand: ").lower()
    
    money_in_bank = hit_or_stand(choice, player_cards, dealer_cards, bet_placed, money_in_bank)

    continue_playing = input("Enter 'yes' if you want to continue playing: ").lower()
    if continue_playing == 'yes':
        play_blackjack(money_in_bank)
    
    print(f"You have ${money_in_bank} left. Thank you for playing!")


#Angela's Solution:
#I used only 1 hint here. Did struggle a little bit but it happened.
"""############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   http://blackjack-final.appbrewery.repl.run

#Hint 2: Read this breakdown of program requirements: 
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Then try to create your own flowchart for the program.

#Hint 3: Download and read this flow chart I've created: 
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

#Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.
import random
from replit import clear
from art import logo

def deal_card():
  ""Returns a random card from the deck.""
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = random.choice(cards)
  return card

#Hint 6: Create a function called calculate_score() that takes a List of cards as input 
#and returns the score. 
#Look up the sum() function to help you do this.
def calculate_score(cards):
  ""Take a list of cards and return the score calculated from the cards""

  #Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.
  if sum(cards) == 21 and len(cards) == 2:
    return 0
  #Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().
  if 11 in cards and sum(cards) > 21:
    cards.remove(11)
    cards.append(1)
  return sum(cards)

#Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.
def compare(user_score, computer_score):
  #Bug fix. If you and the computer are both over, you lose.
  if user_score > 21 and computer_score > 21:
    return "You went over. You lose 😤"


  if user_score == computer_score:
    return "Draw 🙃"
  elif computer_score == 0:
    return "Lose, opponent has Blackjack 😱"
  elif user_score == 0:
    return "Win with a Blackjack 😎"
  elif user_score > 21:
    return "You went over. You lose 😭"
  elif computer_score > 21:
    return "Opponent went over. You win 😁"
  elif user_score > computer_score:
    return "You win 😃"
  else:
    return "You lose 😤"

def play_game():

  print(logo)

  #Hint 5: Deal the user and computer 2 cards each using deal_card()
  user_cards = []
  computer_cards = []
  is_game_over = False

  for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())

  #Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

  while not is_game_over:
    #Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    print(f"   Your cards: {user_cards}, current score: {user_score}")
    print(f"   Computer's first card: {computer_cards[0]}")

    if user_score == 0 or computer_score == 0 or user_score > 21:
      is_game_over = True
    else:
      #Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.
      user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
      if user_should_deal == "y":
        user_cards.append(deal_card())
      else:
        is_game_over = True

  #Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.
  while computer_score != 0 and computer_score < 17:
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)

  print(f"   Your final hand: {user_cards}, final score: {user_score}")
  print(f"   Computer's final hand: {computer_cards}, final score: {computer_score}")
  print(compare(user_score, computer_score))

#Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.
while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
  clear()
  play_game()
"""