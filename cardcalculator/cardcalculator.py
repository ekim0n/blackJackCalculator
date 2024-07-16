def card_value(card):
    ##Assign Hi-Lo values to the cards.
    if card in ['2', '3', '4', '5', '6']:
        return 1
    elif card in ['7', '8', '9']:
        return 0
    elif card in ['10', 'J', 'Q', 'K', 'A']:
        return -1
    else:
        raise ValueError("Invalid card value")
    
def running_count (cards):
    ##count from a list of dealt cards.
    return sum(card_value(card)for card in cards)

def true_count(running_count, decks_remaining):
    ##calculates the true count from the running count and the number of decks remaining.
    if decks_remaining <= 0:
        raise ValueError("Number of decks remaining must be greater than 0")
    return running_count / decks_remaining

def basic_strategy(player_cards, dealer_card):
    ## basicblackjack strategy advice based on players's hand and dealers visible cards
    player_total = sum(min(10, int(card)) if card.isdigit() else 10 if card in ['J', 'Q', 'K'] else 11 for card in player_cards)
    soft = any(card == 'A' for card in player_cards)

    if soft and player_total <= 17:
        return "Hit"
    if player_total >= 17:
        return "Stand"
    if player_total >= 12 and dealer_card in ['4', '5', '6']:
        return "Stand"
    return "Hit"

def get_cards():
    ##Ask the user for the dealer's and player's cards.
    decks_remaining = int(input("Enter number of decks used: "))
    dealer_card = input("Enter dealer's visible card: ").upper()
    player_card = input("Enter players cards separated by space: ").upper().split()
    return dealer_card, player_card, decks_remaining

# Get cards
dealer_card, player_cards, decks_remaining = get_cards()
cards_dealt = [dealer_card] + player_cards

# Calculate running count
r_count = running_count(cards_dealt)
print(f"Running Count: {r_count}")

# Calculate true count (for multiple decks)
t_count = true_count(r_count, decks_remaining)
print(f"True Count: {t_count:.2f}")

# Provide basic strategy advice
advice = basic_strategy(player_cards, dealer_card)
print(f"Player should: {advice}")

