#! usr/bin/env/python

from src.tic_tac_toe import Board, Player
import random


def start_new_game():

    print "\nTime to play some Tic Tac Toe!\n\n"

    print '\t\tUse the layout below to make your move.\n'
    print '''\t\tPress the number on the keyboard that corresponds 
                to the space you want to choose.\n'''

    print """
        \t[7]\t|\t[8]\t|\t[9]
        -------------------------------------------
        \t[4]\t|\t[5]\t|\t[6]
        -------------------------------------------
        \t[1]\t|\t[2]\t|\t[3]\n
    """

def game_over(winner_mark):
    if winner_mark is None:
        print "Cat Game!  You got lucky!"
    else:
        print "{winner} Wins!! Thanks for playing!".format(winner=winner_mark)
    return exit()


def counter_first_move(player_first_move, center, corners):
    if player_first_move == '5':
        computer_move = random.choice(corners)
    else:
        computer_move = center

    return computer_move


def counter_second_move(player_second_move, edges, corners):
    if player_second_move not in corners:
        computer_move = random.choice(edges)
    else:
        computer_move = random.choice(corners)

    return computer_move


def computer_move(available_spaces):
    if len(available_spaces) == 0:
        return None
    else:
        return random.choice(available_spaces)


def prevent_win(space, player_mark, possible_wins):
    """Checks for and blocks possible wins"""
    space_to_update = None
    for pw in possible_wins:
        if space[pw[0]] == player_mark and space[pw[1]] == player_mark and space[pw[2]] == ' ':
            space_to_update = pw[2]
            
    return space_to_update


def go_for_win(space, computer_mark, possible_wins):
    """ Computer will take the win if it can. """
    space_to_update = None
    for pw in possible_wins:
        if space[pw[0]] == computer_mark and space[pw[1]] == computer_mark and space[pw[2]] == ' ':
            space_to_update = pw[2]

    return space_to_update



if __name__ == '__main__':
    start_new_game()
    p = Player()
    b = Board()

    first_move = p.move(b.available_spaces())
    b.update(first_move, p.player_mark)
    counter_first = counter_first_move(first_move, 
                                       b.center, 
                                       b.available_corners(b.available_spaces()))
    b.update(counter_first, b.computer_mark)
    b.display()

    second_move = p.move(b.available_spaces())
    b.update(second_move, p.player_mark)
    prevent = prevent_win(b.spaces, p.player_mark, b.possible_wins)
    if prevent is None:
        counter_second = counter_second_move(second_move, 
                                             b.available_edges(b.available_spaces()), 
                                             b.available_corners(b.available_spaces()))
        b.update(counter_second, b.computer_mark)
    else:
        b.update(prevent, b.computer_mark)
    b.display()
    
    for space in b.available_spaces():
        player_move = p.move(b.available_spaces())
        b.update(player_move, p.player_mark)
        # go for win here
        take_win = go_for_win(b.spaces, b.computer_mark, b.possible_wins)
        if take_win is None:
            prevent = prevent_win(b.spaces, p.player_mark, b.possible_wins)
            if prevent is None:
                cm = computer_move(b.available_spaces())
                if cm is None:
                    winner = None
                    b.display()
                    game_over(winner)
                b.update(cm, b.computer_mark)
                b.display()
            else:
                b.update(prevent, b.computer_mark)
                b.display()
        else:
            b.update(take_win, b.computer_mark)
            winner = b.get_winner()
            b.display()
            game_over(winner)
    
    