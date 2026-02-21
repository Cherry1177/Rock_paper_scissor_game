EMOJI_MAP = {
   "rock" : "✊",
   "paper" : "👋",
   "scissors" : "✌️"
}

import random
from game_logic import determine_winner
from player import get_user_input
from computer import get_computer_choice


def get_emoji(choice):
    return EMOJI_MAP.get(choice)

user_choice=""
def welcome_user():
    print("Welcome to Rock, Paper, Scissors!")

welcome_user()

valid_choices = ['rock', 'paper', 'scissors','r','p','s']
computer_choices = ['rock', 'paper', 'scissors']

player_score = 0
computer_score = 0
play_again = "yes"

while play_again == "yes":
    user_choice = get_user_input(valid_choices)
    print(f"You chose: {get_emoji(user_choice)}")
    computer_choice = get_computer_choice(computer_choices)
    print(f"Computer chose: {get_emoji(computer_choice)}")
    result = determine_winner(user_choice, computer_choice)
    print(result)
    if(result == "You win!"):
        player_score = player_score + 1
    elif(result == "You lose!"):
        computer_score = computer_score + 1
    else:
        player_score += 0
        computer_score += 0
    print(f"Your score: {player_score}")
    print(f"Computer score: {computer_score}")
    play_again = input("Do you want to play again? (yes/no): ")

print("Thank you for playing")

    