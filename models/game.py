from models.player import *

player_list = []

def add_player(player_object):
    player_list.append(player_object)
    print(player_list)

def play_game(player_1, player_2):
    winner = None
    if player_1 == 'rock' and player_2 == 'scissors':
        winner = True
    elif player_1 == 'rock' and player_2 == 'paper':
        winner = False
    elif player_1 == 'paper' and player_2 == 'scissors':
        winner = False
    elif player_1 == 'paper' and player_2 == 'rock':
        winner = True
    elif player_1 == 'scissors' and player_2 == 'paper':
        winner == True
    elif player_1 == 'scissors' and player_2 == 'rock':
        winner = False
    else:
        winner = None
    return winner

def clear_player_list(player_list):
    player_list.clear()
