SHORTCUTS = {
    "r" : "rock",
    "p" : "paper",
    "s" : "scissors"
}
def get_user_input(valid_choices):
    user_choice = input("Enter r for rock, p for paper, or s for scissors: ").lower()

    while(user_choice not in valid_choices):
        print("Oops! That's not a valid move. Please enter r for rock, p for paper, or s for scissors.")
        user_choice = input("Enter rock, paper, or scissors: ").lower()
        
    if user_choice in valid_choices:
        return SHORTCUTS.get(user_choice)
        