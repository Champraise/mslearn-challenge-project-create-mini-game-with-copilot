# function that takes two arguments, in the options of rock, paper, scissors and returns a string stating the winner
def determine_winner(user_choice, computer_choice):
    """
    This function takes two arguments, in the options of rock, paper, scissors and returns a string stating the winner
    :param user_choice: string
    :param computer_choice: string
    :return: string
    """
    # if the user and computer choice are the same, return a string stating that it is a tie
    if user_choice == computer_choice:
        return "It's a tie!"
    # if the user choice is rock and the computer choice is scissors, return a string stating that the user won
    elif user_choice == "rock" and computer_choice == "scissors":
        return "You won!"
    # if the user choice is paper and the computer choice is rock, return a string stating that the user won
    elif user_choice == "paper" and computer_choice == "rock":
        return "You won!"
    # if the user choice is scissors and the computer choice is paper, return a string stating that the user won
    elif user_choice == "scissors" and computer_choice == "paper":
        return "You won!"
    # if the user choice is rock and the computer choice is paper, return a string stating that the computer won
    elif user_choice == "rock" and computer_choice == "paper":
        return "You lost!"
    # if the user choice is paper and the computer choice is scissors, return a string stating that the computer won
    elif user_choice == "paper" and computer_choice == "scissors":
        return "You lost!"
    # if the user choice is scissors and the computer choice is rock, return a string stating that the computer won
    elif user_choice == "scissors" and computer_choice == "rock":
        return "You lost!"
    # if the user choice is not rock, paper, or scissors, return a string stating that the user choice is invalid
    else:
        return "Invalid choice!"

# function that prompts the user to enter a choice of rock, paper, or scissors
def get_user_choice():
    """
    This function prompts the user to enter a choice of rock, paper, or scissors
    :return: string
    """
    # prompt the user to enter a choice of rock, paper, or scissors
    user_choice = input("Enter rock, paper, or scissors: ")
    # return the user choice
    return user_choice

# function that randomly generates a choice of rock, paper, or scissors for the computer
def get_computer_choice():
    """
    This function randomly generates a choice of rock, paper, or scissors for the computer
    :return: string
    """
    # import the random module
    import random
    # generate a random integer between 1 and 3
    random_integer = random.randint(1, 3)
    # if the random integer is 1, return rock
    if random_integer == 1:
        return "rock"
    # if the random integer is 2, return paper
    elif random_integer == 2:
        return "paper"
    # if the random integer is 3, return scissors
    else:
        return "scissors"

# function that prints the user choice, computer choice, and winner
def print_choices(user_choice, computer_choice, winner):
    """
    This function prints the user choice, computer choice, and winner
    :param user_choice: string
    :param computer_choice: string
    :param winner: string
    :return: none
    """
    # print the user choice, computer choice, and winner
    print("You chose " + user_choice + ".")
    print("The computer chose " + computer_choice + ".")
    print(winner)

# function that runs the game and updates the score for each round and the total score
def run_game():
    """
    This function runs the game and updates the score for each round and the total score
    :return: none
    """
    # initialize the round number to 1
    round_number = 1
    # initialize the total score to 0
    total_score = 0
    # while the round number is less than or equal to 3
    while round_number <= 3:
        # print the round number
        print("Round " + str(round_number) + ":")
        # get the user choice
        user_choice = get_user_choice()
        # get the computer choice
        computer_choice = get_computer_choice()
        # determine the winner
        winner = determine_winner(user_choice, computer_choice)
        # print the user choice, computer choice, and winner
        print_choices(user_choice, computer_choice, winner)
        # if the winner is "You won!", add 1 to the total score
        if winner == "You won!":
            total_score += 1
        # add 1 to the round number
        round_number += 1
    # print the total score
    print("Total score: " + str(total_score))

# call the run_game function
run_game()