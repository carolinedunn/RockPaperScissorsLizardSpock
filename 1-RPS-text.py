# Imports ---------------
from guizero import App, Box, PushButton, Text
from random import choice

# Global Variables -------------
choices = ["rock", "paper", "scissors"]

# Functions -------------

def get_winner(user_pick):
    computer_pick = choice(choices)
    message.value = "Computer picks " + computer_pick
    if user_pick == computer_pick:
        message.value += ". It's a draw."
    elif (user_pick == "scissors"):
        if (computer_pick == "paper"):
            message.value += ". Scissors cuts paper. You win!"
        else: #computer picks rock
            message.value += ". Rock beats scissors. Computer wins."
    elif (user_pick == "rock"):
        if (computer_pick == "scissors"):
            message.value += ". Rock beats scissors. You win!"
        else: #computer picks paper
            message.value += ". Paper covers rock. Computer wins."    
    elif (user_pick == "paper"):
        if (computer_pick == "rock"):
            message.value += ". Paper covers rock. You win!"
        else: #computer picks scissors
            message.value += ". Scissors cuts paper. Computer wins." 
    else:
        message.value = "oops, error "

# App -------------------
app = App("Rock Paper Scissors")
title = Text(app, "Choose Rock Paper or Scissors")
board = Box(app, layout="grid")
rock = PushButton(board, command=get_winner, args=["rock"], text = "Rock", grid=[0,0])
paper = PushButton(board, command=get_winner, args=["paper"], text = "Paper", grid=[1,0])
scissors = PushButton(board, command=get_winner, args=["scissors"], text = "Scissors", grid=[2,0])
message = Text(app)
app.display()
