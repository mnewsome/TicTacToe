#! usr/bin/env/python
from ui import ConsoleUI

console = ConsoleUI()


class Board(object):
    def __init__(self):
        self.spaces = {
                 '1': ' ', 
                 '2': ' ',
                 '3': ' ',
                 '4': ' ',
                 '5': ' ',
                 '6': ' ',
                 '7': ' ',
                 '8': ' ',
                 '9': ' ',
                 }

        self.center = '5'
        self.edges = ['2', '4', '6', '8']
        self.corners = ['1', '3', '7', '9']

        # (space to check, space to check, move)
        self.possible_wins = (
                     ('5', '1', '9'),
                     ('5', '2', '8'),
                     ('5', '3', '7'),
                     ('5', '4', '6'),
                     ('5', '6', '4'),
                     ('5', '7', '3'),
                     ('5', '8', '2'),
                     ('5', '9', '1'),
                     ('1', '2', '3'),
                     ('1', '3', '2'),
                     ('1', '4', '7'),
                     ('1', '7', '4'),
                     ('1', '9', '5'),
                     ('2', '3', '1'),
                     ('2', '8', '5'),
                     ('3', '6', '9'),
                     ('3', '7', '5'),
                     ('3', '9', '6'),
                     ('4', '6', '5'),
                     ('4', '7', '1'),
                     ('6', '9', '3'),
                     ('7', '8', '9'),
                     ('7', '9', '8'),
                     ('8', '9', '7'),
                     )

        #(space to check, space to check, move)
        self.check_edges = (
                   ('2', '4', '1'),
                   ('2', '6', '3'),
                   ('4', '8', '7'),
                   ('6', '8', '9'),
                   )

    def update(self, move, player_mark):
        """ Updates the current state of the board"""
        self.spaces[move] = player_mark

    def display(self):
        """Displays the current state of the board"""
        board = """
        \t{seven}\t|\t{eight}\t|\t{nine}
        ------------------------------------------------
        \t{four}\t|\t{five}\t|\t{six}
        ------------------------------------------------
        \t{one}\t|\t{two}\t|\t{three}
        \n
        \n
        Available spaces: {available_spaces}
        """.format(one=self.spaces['1'], two=self.spaces['2'], three=self.spaces['3'],
                   four=self.spaces['4'], five=self.spaces['5'], six=self.spaces['6'],
                   seven=self.spaces['7'], eight=self.spaces['8'], nine=self.spaces['9'],
                   available_spaces=self.available_spaces())

        return console.display_data(board)

    def available_spaces(self):
        """ Returns list of available moves """
        available_spaces = []
        for key,value in self.spaces.iteritems():
            if value == ' ':
                available_spaces.append(key)
        return sorted(available_spaces)

    def available_edges(self):
        available_spaces= self.available_spaces()
        self.edges = [edge for edge in self.edges if edge in available_spaces]
        return self.edges

    def available_corners(self):
        available_spaces= self.available_spaces()
        self.corners = [corner for corner in self.corners if corner in available_spaces]
        return self.corners

    def check_for_win(self, row):
        """Returns true if all player marks are the same"""
        return all(mark == row[0] for mark in row)

    def get_winner (self):
        bottom_row = [self.spaces['1'], self.spaces['2'], self.spaces['3']]
        middle_row = [self.spaces['4'], self.spaces['5'], self.spaces['6']]
        top_row = [self.spaces['7'], self.spaces['8'], self.spaces['9']]
        left_column = [self.spaces['7'], self.spaces['4'], self.spaces['1']]
        middle_column = [self.spaces['8'], self.spaces['5'], self.spaces['2']]
        right_column = [self.spaces['9'], self.spaces['6'], self.spaces['3']]
        left_diagonal = [self.spaces['7'], self.spaces['5'], self.spaces['3']]
        right_diagonal = [self.spaces['9'], self.spaces['5'], self.spaces['1']]
        
        all_combinations = [
                            bottom_row, 
                            middle_row, 
                            top_row, 
                            left_column, 
                            middle_column, 
                            right_column, 
                            left_diagonal, 
                            right_diagonal
                            ]
        winner = None
        for combo in all_combinations:
            if ' ' not in combo:
                if self.check_for_win(combo):
                    winner = combo[0]
        
        return winner

    def is_first_move(self, available_spaces):
        """ Returns true if it is player's first move. Else false. """
        return len(available_spaces) == 9

    def is_move_valid(self, selection, available_spaces):
        """ Returns true if player selects an available space. Else false. """
        return selection in available_spaces