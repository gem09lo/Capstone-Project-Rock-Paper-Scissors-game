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

def play_again():
    return input("Play again?(y/n): ")

def game():
    while True:
        user = users_hand()
        computer = computers_hand()
        print("Computer drew {} \nYou drew {}".format(computer, user))

        if user == computer:
            print("Draw")
        elif user == "rock" and computer == "scissors":
            print("You win!")
        elif user == "paper" and computer == "rock":
            print("You win!")
        elif user == "scissors" and computer == "paper":
            print("You win!")
        else:
            print("You lose!")

        play_again = input("Play again?(y/n): ")
        if play_again == "n":
            break


game()
