EMOJI_MAP = {
   "rock" : "✊",
   "paper" : "👋",
   "scissors" : "✌️"
}

import random
from game_logic import determine_winner
from player import get_user_input
from computer import get_computer_choice

play_again = "yes"

def get_emoji(choice):
    return EMOJI_MAP.get(choice)

user_choice=""
def welcome_user():
    print("Welcome to Rock, Paper, Scissors!")

welcome_user()

valid_choices =['rock', 'paper', 'scissors']

def round (play_again):
    user_choice = get_user_input(valid_choices)
    computer_choice = get_computer_choice(valid_choices)
    result = determine_winner(user_choice, computer_choice)
    print(f"You chose: {get_emoji(user_choice)}")
    print(f"Computer chose: {get_emoji(computer_choice)}")
    print(result)

round(play_again)

play_again = input("Do you want to play again? (yes/no): ")

while(play_again == "yes"):
    round(play_again)
    play_again = input("Do you want to play again? (yes/no): ")

while(play_again == "no"):
    print("Thank you for playing")
    exit()
    