import random
import math

def get_user_pick(show1, show2):
    """
    Prompts the user to pick between two shows.
    """
    while True:
        print(f"\n  👶 Time to pick! Which one does the 3-year-old want to watch?")
        print(f"  1. '{show1}'")
        print(f"  2. '{show2}'")
        choice = input("  Type the full name of the chosen show (e.g., 'Dinosaurs' or 'Peppa Pig'): ").strip()

        if choice.lower() == show1.lower():
            print(f"  🎉 Great choice! '{show1}' it is!")
            return show1
        elif choice.lower() == show2.lower():
            print(f"  🎉 Great choice! '{show2}' it is!")
            return show2
        else:
            print("  🤔 That's not one of the options. Please type the name exactly as shown (case-insensitive).")

def run_sequential_challenge(shows):
    """
    Runs a sequential challenge process where the winner faces the next show.
    The first show in the list starts as the champion.
    """
    if not shows:
        print("No shows provided to pick from!")
        return None

    current_champion = shows[0]
    print("--- Starting the TV Show Sequential Challenge! ---")
    print(f"Initial champion: '{current_champion}'\n")

    # Iterate through the rest of the shows, each one challenging the current champion
    for i in range(1, len(shows)):
        challenger = shows[i]
        print(f"--- Challenge {i} ---")
        print(f"  Current Champion: '{current_champion}'")
        print(f"  Challenger: '{challenger}'")

        winner = get_user_pick(current_champion, challenger)
        print("-" * 30) # Separator for clarity

        if winner != current_champion:
            print(f"  👑 New champion! '{winner}' has defeated '{current_champion}'.")
            current_champion = winner
        else:
            print(f"  🛡️ '{current_champion}' defends the title against '{challenger}'.")
        print("\n") # Add extra line for readability between challenges

    final_winner = current_champion
    print("--- Sequential Challenge Concluded! ---")
    print(f"🏆 The ultimate winner for the 3-year-old to watch is: '{final_winner}'! 🏆")
    return final_winner

if __name__ == "__main__":
    # Define the initial list of TV shows
    tv_shows = ["Dinosaurs", "Peppa Pig", "Kids2Kids", "Bluey", "King Estate"]

    # Run the sequential challenge
    final_choice = run_sequential_challenge(tv_shows)
