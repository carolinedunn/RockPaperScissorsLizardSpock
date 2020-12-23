# Imports ---------------
from guizero import App, Box, PushButton, Text
from random import choice

# Global Variables -------------
choices = ["rock", "paper", "scissors", "lizard", "spock"]

# Functions -------------
def clear_board():
    new_board = [[None, None, None, None, None]]
    title = Text(app, "Choose Rock, Paper, Scissors, Lizard, or Spock")
    board = Box(app, layout="grid")
    rock = PushButton(board, command=get_winner, args=["rock"], image = "rock.png", grid=[0,0])
    paper = PushButton(board, command=get_winner, args=["paper"], image = "paper.png", grid=[1,0])
    scissors = PushButton(board, command=get_winner, args=["scissors"], image = "scissors.png", grid=[2,0])
    lizard = PushButton(board, command=get_winner, args=["lizard"], image = "lizard.png", grid=[3,0])
    spock = PushButton(board, command=get_winner, args=["spock"], image = "spock.png", grid=[4,0])
    
    return new_board

def get_winner(user_pick):
    computer_pick = choice(choices)
    message.value = "Computer picks " + computer_pick
    if user_pick == computer_pick:
        message.value += ". It's a draw."
    elif (user_pick == "scissors"):
        if (computer_pick == "paper"):
            message.value += ". Scissors cuts paper. You win!"
            you.value = int(you.value) + 1
        elif (computer_pick == "rock"):
            message.value += ". Rock beats scissors. Computer wins."
            computer.value = int(computer.value) + 1
        elif (computer_pick == "lizard"):
            message.value += ". Scissors cuts lizard. You win!"
            you.value = int(you.value) + 1
        else: #computer picks spock
            message.value += ". Spock smashes scissors. Computer wins."
            computer.value = int(computer.value) + 1
    elif (user_pick == "rock"):
        if (computer_pick == "scissors"):
            message.value += ". Rock beats scissors. You win!"
            you.value = int(you.value) + 1
        elif (computer_pick == "paper"):
            message.value += ". Paper covers rock. Computer wins."
            computer.value = int(computer.value) + 1
        elif (computer_pick == "lizard"):
            message.value += ". Rock crushes lizard. You win!"
            you.value = int(you.value) + 1
        else: #computer picks spock
            message.value += ". Spock vaporizes rock. Computer wins."
            computer.value = int(computer.value) + 1
    elif (user_pick == "paper"):
        if (computer_pick == "rock"):
            message.value += ". Paper covers rock. You win!"
            you.value = int(you.value) + 1
        elif (computer_pick == "scissors"):
            message.value += ". Scissors cuts paper. Computer wins."
            computer.value = int(computer.value) + 1
        elif (computer_pick == "lizard"):
            message.value += ". Lizard eats paper. Computer wins."
            computer.value = int(computer.value) + 1
        else: #computer picks spock
            message.value += ". Paper disproves Spock. You win!"
            you.value = int(you.value) + 1
    elif (user_pick == "lizard"):
        if (computer_pick == "paper"):
            message.value += ". Lizard eats paper. You win!"
            you.value = int(you.value) + 1
        elif (computer_pick == "rock"):
            message.value += ". Rock crushes lizard. Computer wins."
            computer.value = int(computer.value) + 1
        elif (computer_pick == "scissors"):
            message.value += ". Scissors cuts lizard. Computer wins."
            computer.value = int(computer.value) + 1           
        else: #computer picks spock
            message.value += ". Lizard poisons Spock. You win!"
            you.value = int(you.value) + 1
    else: #user picks spock
        if (computer_pick == "rock"):
            message.value += ". Spock vaporizes rock. You win!"
            you.value = int(you.value) + 1
        elif (computer_pick == "scissors"):
            message.value += ". Spock smashes scissors. You win!"
            you.value = int(you.value) + 1            
        elif (computer_pick == "lizard"):
            message.value += ". Lizard poisons Spock. Computer wins."
            computer.value = int(computer.value) + 1
        else: #computer picks paper
            message.value += ". Paper disproves Spock. Computer wins."
            computer.value = int(computer.value) + 1

def reset_score():
    computer.value = "0"
    you.value = "0"

# App -------------------
app = App("Rock Paper Scissors Lizard Spock")
game_box = Box(app, align="top")
Text(game_box, text="Scoreboard", align="top")
Text(game_box, align="left", text="You: ")
you = Text(game_box, text="0", align="left")
computer = Text(game_box, text="0", align="right")
Text(game_box, text="Computer: ", align="right")
clear_board()

message = Text(app)
reset = PushButton(app, command=reset_score, text = "Reset Scoreboard")
app.display()

