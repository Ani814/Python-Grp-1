"""
Lottery Simulator
- Computer picks 6 numbers from 1-49
- Player enters 6 numbers
- Count matches and award based on jackpot
- Logs each draw to lottery.log
"""

import random
import logging

# Setup logging
logger = logging.getLogger("lottery")
logger.setLevel(logging.INFO)
if not logger.handlers:
    fh = logging.FileHandler("lottery.log", encoding="utf-8")
    fh.setFormatter(logging.Formatter("%(asctime)s - %(message)s"))
    logger.addHandler(fh)

JACKPOT = 1000000  # initial jackpot

def draw_winning_numbers():
    return sorted(random.sample(range(1, 50), 6))

def get_player_numbers():
    print("Enter 6 numbers between 1 and 49 (separated by spaces):")
    while True:
        try:
            raw = input().strip().split()
            if len(raw) != 6:
                print("Exactly 6 numbers required.")
                continue
            nums = [int(x) for x in raw]
            if any(n < 1 or n > 49 for n in nums):
                print("All numbers must be between 1 and 49.")
                continue
            if len(set(nums)) != 6:
                print("Numbers must be unique.")
                continue
            return sorted(nums)
        except ValueError:
            print("Please enter valid integers.")

def calculate_prize(matches):
    global JACKPOT
    if matches == 6:
        prize = JACKPOT
        JACKPOT = 0  # reset? Actually we can keep it 0 and later add funds? The spec says we "subtract" from jackpot, we'll set to remaining.
        # According to spec: if 6-6 -> jackpot won, we set jackpot to 0 (or we can define new jackpot later)
        # But we need to subtract percentages for other matches.
        # We'll do accordingly.
    elif matches == 5:
        prize = JACKPOT * 0.4  # 40% of jackpot
        JACKPOT -= prize
    elif matches == 4:
        prize = JACKPOT * 0.6
        JACKPOT -= prize
    elif matches == 3:
        prize = JACKPOT * 0.8
        JACKPOT -= prize
    else:
        prize = 0
    # For matches 1 or 2, prize = 0, no jackpot change.
    return round(prize, 2)

def play_round():
    winning = draw_winning_numbers()
    print(f"Winning numbers: {winning}")
    player_nums = get_player_numbers()
    matches = len(set(winning) & set(player_nums))
    print(f"You matched {matches} number(s).")
    prize = calculate_prize(matches)
    if prize > 0:
        print(f"You win {prize:.2f} GEL!")
        # Log the win
        logger.info(f"Player {player_nums} matched {matches} numbers, won {prize} GEL")
    else:
        print("Sorry, you win nothing this time.")
        logger.info(f"Player {player_nums} matched {matches} numbers, no prize")
    print(f"Current jackpot: {JACKPOT:.2f} GEL")
    return prize

def main():
    global JACKPOT
    print("\n===== Lottery Simulator =====")
    print(f"Starting jackpot: {JACKPOT:.2f} GEL")
    while True:
        play_round()
        again = input("\nPlay again? (y/n): ").strip().lower()
        if again != 'y':
            break
    print("Thanks for playing!")

if __name__ == "__main__":
    main()