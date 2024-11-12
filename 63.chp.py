import random

# Function to get computer's choice
def get_computer_choice():
    choices = ["S", "W", "G"]  # S for Snake, W for Water, G for Gun
    return random.choice(choices)

# Function to determine the winner
def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "Draw"
    elif (player_choice == "S" and computer_choice == "W") or \
         (player_choice == "W" and computer_choice == "G") or \
         (player_choice == "G" and computer_choice == "S"):
        return "Player wins"
    else:
        return "Computer wins"

# Main function to play the game
def main():
    print("Welcome to Snake Water Gun game!")
    print("Your choices are: S for Snake, W for Water, G for Gun")

    player_choice = input("Enter your move (S, W, G): ").upper()
    if player_choice not in ["S", "W", "G"]:
        print("Invalid choice! Please enter S, W, or G.")
        return

    computer_choice = get_computer_choice()
    print(f"Computer chose: {computer_choice}")

    result = determine_winner(player_choice, computer_choice)
    print(result)

if __name__ == "__main__":
    main()
