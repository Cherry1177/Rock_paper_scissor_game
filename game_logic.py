def determine_winner(user_choice, computer_choice):
    if(user_choice == computer_choice):
        result = "Draw!"
        return result

    elif(user_choice == "rock" and computer_choice=="scissors") or (user_choice == "scissors" and computer_choice=="paper")or(user_choice=="paper" and computer_choice=="rock"):
        result = "You win!"
        return result

    elif(user_choice == "scissors" and computer_choice=="paper"):
        result="You win!"
        return result
    elif(user_choice == "paper" and computer_choice=="rock"):
        result="You win!"
        return result
    else:
        result = "You lose!"
        return result