from flask import render_template, request, redirect
from app import app
from models.game import *
from models.player import *

@app.route('/rpshome')
def index():
    clear_player_list(player_list)
    return render_template('index.html', title="Rock, Paper, Scissors - Home", player_list=player_list)

@app.route('/rpshome/player_2', methods=['POST'])
def player_1_chosen():
    name = request.form['name']
    choice = request.form['choice']
    player_1 = Player(name, choice)
    add_player(player_1)
    return render_template('player_2.html', title="Player 2 Go", player_list=player_list)

@app.route('/rpshome/result', methods=['POST'])
def game_result():
    name = request.form['name']
    choice = request.form['choice']
    player_2 = Player(name, choice)
    add_player(player_2)
    player_1_choice = player_list[0].choice
    player_2_choice = player_list[1].choice
    winner = play_game(player_1_choice, player_2_choice)
    return render_template('result.html', title="The Result is in!", winner=winner, player_list=player_list)