#! usr/bin/env/python
import random

from src.board import Board
from src.player import Player, ComputerPlayer
from ui import ConsoleUI

console = ConsoleUI()

def start_new_game():
    board = ("""
    \nTime to play some Tic Tac Toe!\n

    \tUse the layout below to make your move.\n
    \tPress the number on the keyboard that corresponds
                to the space you want to choose.\n

        \t[7]\t|\t[8]\t|\t[9]
        -------------------------------------------
        \t[4]\t|\t[5]\t|\t[6]
        -------------------------------------------
        \t[1]\t|\t[2]\t|\t[3]\n
    """
    )
    console.display_data(board)

def game_over(winner_mark, player_mark=None):
    if winner_mark is None:
        console.display_data("Cat Game!  You got lucky!")
    elif winner_mark == player_mark:
        console.display_data("{winner} Wins?! That's not suppsed to happen!".format(winner=winner_mark))
    else:
        console.display_data("{winner} Wins!! Thanks for playing!".format(winner=winner_mark))
    return exit()

def set_marks():
    player_mark_choice = ''
    mark_choices = ('X','O')
    while player_mark_choice not in mark_choices:
        prompt = "Choose your game piece: {0}".format(mark_choices)
        player_mark_choice = console.get_input(prompt).upper()
    if player_mark_choice == 'X':
        computer_mark = 'O'
    else:
        computer_mark = 'X'
    return dict(player_mark=player_mark_choice, computer_mark=computer_mark)

def player_move():
    move = ''
    while not b.is_move_valid(move, b.available_spaces()):
        move = p.move(b.is_first_move(b.available_spaces()))
    b.update(move, p.mark)
    return move

def counter_move(first_move, second_move=None):
    if second_move is None:
        counter = c.counter_first_move(first_move, 
                                       b.center, 
                                       b.available_corners())
        b.update(counter, c.mark)
    else:
        counter = c.counter_second_move(first_move,
                                         second_move, 
                                         b.available_edges(), 
                                         b.available_corners(),
                                         b.check_edges,
                                         )
        b.update(counter, c.mark)
    return counter

if __name__ == '__main__':
    start_new_game()
    mark = set_marks()
    p = Player(mark["player_mark"])
    c = ComputerPlayer(mark["computer_mark"])
    b = Board()

    first_move = player_move()
    counter_move(first_move)
    b.display()
    second_move = player_move()

    prevent = c.prevent_win(b.spaces, p.mark, b.possible_wins)
    if prevent is None:
        counter = counter_move(first_move, second_move)
    else:
        b.update(prevent, c.mark)
    b.display()

    for space in b.available_spaces():
        player_move()
        # go for win here
        take_win = c.go_for_win(b.spaces, c.mark, b.possible_wins)
        if take_win is None:
            prevent = c.prevent_win(b.spaces, p.mark, b.possible_wins)
            if prevent is None:
                cm = c.move(b.available_spaces())
                if cm is None:
                    winner = None
                    b.display()
                    game_over(winner)
                winner = b.get_winner()
                if winner == p.mark:
                    b.display()
                    game_over(winner, player_mark=p.mark)
                b.update(cm, c.mark)
                b.display()
            else:
                b.update(prevent, c.mark)
                b.display()
        else:
            b.update(take_win, c.mark)
            winner = b.get_winner()
            b.display()
            game_over(winner)