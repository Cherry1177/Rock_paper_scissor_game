EMOJI_MAP = {
   "rock" : "✊",
   "paper" : "👋",
   "scissors" : "✌️"
}

from game_logic import determine_winner
from player import get_user_input
from computer import get_computer_choice

def get_emoji(choice):
    return EMOJI_MAP.get(choice)

user_choice=""
def welcome_user():
    print("Welcome to Rock, Paper, Scissors!")

welcome_user()

valid_choices =['rock', 'paper', 'scissors']

user_choice = get_user_input(valid_choices)

computer_choice = get_computer_choice(valid_choices)

result = determine_winner(user_choice, computer_choice)

print(f"You chose: {get_emoji(user_choice)}")
print(f"Computer chose: {get_emoji(computer_choice)}")
print(result)