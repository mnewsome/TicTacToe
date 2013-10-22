#! usr/bin/env/python
import random
from ui import ConsoleUI
from board import Board

console = ConsoleUI()
b = Board()

class Player(object):
    """ Human Player """
    def __init__(self, mark):
        self.mark = mark

    def move(self, first_move=False):
        move = ''
        if first_move:
            console.display_data("\nMake your first move...\nYou will be {0}".format(self.mark))
            prompt = "\nWhere would you like to go first?\nEnter a number (1-9) >> "
            move = console.get_input(prompt)
            return move
        else:
            prompt = "\nWhere would you like to go next? >> "
            move = console.get_input(prompt)
            return move


class ComputerPlayer(Player):
    """ AI that represents Computer Player"""
    def move(self, available_spaces):
        if len(available_spaces) == 0:
            return None
        else:
            return random.choice(available_spaces)

    def counter_first_move(self, player_first_move, center, corners):
        if player_first_move == '5':
            computer_move = random.choice(corners)
        else:
            computer_move = center
        return computer_move

    def counter_second_move(self, player_first_move, player_second_move, edges, corners, check_edges):
        computer_move = ''
        if b.is_edge(player_first_move) and b.is_edge(player_second_move):
            for e in check_edges:
                if e[0] not in edges and e[1] not in edges:
                    computer_move = e[2]
        elif player_second_move not in corners:
            if player_first_move is '5':
                computer_move = random.choice(corners)
            else:
                computer_move = random.choice(edges)
        else:
            computer_move = random.choice(corners)
        return computer_move

    def prevent_win(self, space, player_mark, possible_wins):
        """Checks for and blocks possible wins"""
        space_to_update = None
        for pw in possible_wins:
            if space[pw[0]] == player_mark and space[pw[1]] == player_mark and space[pw[2]] == ' ':
                space_to_update = pw[2]           
        return space_to_update

    def go_for_win(self, space, computer_mark, possible_wins):
        """ Computer will take the win if it can. """
        space_to_update = None
        for pw in possible_wins:
            if space[pw[0]] == computer_mark and space[pw[1]] == computer_mark and space[pw[2]] == ' ':
                space_to_update = pw[2]
        return space_to_update