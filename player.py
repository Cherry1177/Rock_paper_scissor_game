def get_user_input(valid_choices):
    user_choice = input("Enter rock, paper, or scissors: ").lower()

    if user_choice in valid_choices:
        return user_choice
    else:
        print("Oops! That's not a valid move.")
        return None