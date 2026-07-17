"""
Game 21 (simplified Blackjack)
- Deck of 52 cards (suits and ranks)
- Player and computer get 2 cards each initially
- Player can 'add' or 'stop'
- Computer adds until score >= 17
- Closest to 21 without exceeding wins
"""

import random

SUITS = ["♠", "♥", "♦", "♣"]
RANKS = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
VALUES = {
    "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9,
    "10": 10, "J": 10, "Q": 10, "K": 10, "A": 11
}

def build_deck():
    deck = []
    for suit in SUITS:
        for rank in RANKS:
            deck.append((rank, suit))
    random.shuffle(deck)
    return deck

def hand_value(hand):
    total = sum(VALUES[card[0]] for card in hand)
    # Ace can be 1 if 11 busts
    aces = sum(1 for card in hand if card[0] == "A")
    while total > 21 and aces > 0:
        total -= 10
        aces -= 1
    return total

def display_hand(hand, hidden=False):
    if hidden:
        return "[?, ?]"
    return " ".join(f"{rank}{suit}" for rank, suit in hand)

def play_game():
    deck = build_deck()
    player_hand = [deck.pop(), deck.pop()]
    computer_hand = [deck.pop(), deck.pop()]

    print("\n===== Game 21 =====")
    print(f"Your hand: {display_hand(player_hand)}  (value: {hand_value(player_hand)})")
    print(f"Computer's hand: {display_hand(computer_hand, hidden=True)}")

    # Player turn
    while True:
        if hand_value(player_hand) > 21:
            print("You bust! You lose.")
            return
        move = input("Do you want to 'add' a card or 'stop'? ").strip().lower()
        if move == "stop":
            break
        elif move == "add":
            player_hand.append(deck.pop())
            print(f"Your hand: {display_hand(player_hand)}  (value: {hand_value(player_hand)})")
        else:
            print("Invalid input. Type 'add' or 'stop'.")

    if hand_value(player_hand) > 21:
        print("You bust! You lose.")
        return

    # Computer turn
    print("\nComputer's turn...")
    while hand_value(computer_hand) < 17:
        computer_hand.append(deck.pop())
    print(f"Computer's hand: {display_hand(computer_hand)}  (value: {hand_value(computer_hand)})")

    player_total = hand_value(player_hand)
    computer_total = hand_value(computer_hand)

    if computer_total > 21:
        print("Computer busts! You win!")
    elif player_total > computer_total:
        print("You win!")
    elif player_total < computer_total:
        print("You lose!")
    else:
        print("It's a tie. Let's play again.")
        play_game()  # restart

def main():
    while True:
        play_game()
        again = input("\nPlay again? (y/n): ").strip().lower()
        if again != 'y':
            break

if __name__ == "__main__":
    main()