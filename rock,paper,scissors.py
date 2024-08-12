#python rock,paper,scissors.py

#rules - Rock smashes scissors, Scissors cuts paper, paper covers rock
# computer hand - import random
# user input hand

import random

possible_hands = ["rock", "paper", "scissors"]

def computers_hand():
    return random.choice(possible_hands)

def users_hand():
    return input("Enter rock, paper or scissors: ")

def ask_for_another_game():
    return input("Play again?(y/n): ")


def game():
    user_score = 0
    computer_score = 0

    while True:
        user = users_hand()
        computer = computers_hand()
        print("Computer drew {} \nYou drew {}".format(computer, user))

        if user == computer:
            print("Draw")
        elif user == "rock" and computer == "scissors":
            print("You win!")
            user_score += 1
        elif user == "paper" and computer == "rock":
            print("You win!")
            user_score += 1
        elif user == "scissors" and computer == "paper":
            print("You win!")
            user_score += 1
        else:
            print("You lose!")
            computer_score += 1
        print ("Computer {}:{} You".format(computer_score, user_score))

        if computer_score == 2:
            print("Computer wins - better luck next time!")
            play_again = ask_for_another_game()
            if play_again == "n":
                break
            else:
                computer_score = 0
                user_score = 0
        elif user_score == 2:
            print("You win! Congratulations!")
            play_again = ask_for_another_game()
            if play_again == "n":
                break
            else:
                computer_score = 0
                user_score = 0


game()
