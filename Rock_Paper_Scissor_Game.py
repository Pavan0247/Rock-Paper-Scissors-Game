import random as r
    # Implementatiom of Rock Paper Scissors Game
    # We are playing Computer vs User
    # Rule Paper > Rock, Scissor > Paper, Rock > Scissor

def play():
    user_choice = input("'r' for Rock, 'p' for Paper, 's' Scissor: \n")
    comp_choice = r.choice(['r', 'p', 's'])
    if user_choice == comp_choice:
        return "It's Tie"
    if win(user_choice, comp_choice):
        return "You Won!"
    return "You Lost!"

def win(player, opponent):
    if (player == 's' and opponent == 'p') or (player == 'r' and opponent == 's') \
       or (player == 'p' and opponent == 'r'):
        return True

print(play())
