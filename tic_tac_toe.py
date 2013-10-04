#! usr/bin/env/python

# Written by Malcolm Newsome -- Canditate for 8th Light Software Apprenticeship 
#
# Contact:  847.732.7641(cell) or malcolm.newsome@g.gmail.com


class Board(object):

    def __init__(self):
        self.space = {
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
        self.computer_mark = 'O'
        self.player_mark = 'X'
        
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

    def update(self, move, player_mark):
        """ Updates the current state of the board"""
        self.space[move] = player_mark


    def display(self):
        """Displays the current state of the board"""

        board = """
        \t{seven}\t|\t{eight}\t|\t{nine}
        ------------------------------------------------
        \t{four}\t|\t{five}\t|\t{six}
        ------------------------------------------------
        \t{one}\t|\t{two}\t|\t{three}
        """.format(one=self.space['1'], two=self.space['2'], three=self.space['3'],
                   four=self.space['4'], five=self.space['5'], six=self.space['6'],
                   seven=self.space['7'], eight=self.space['8'], nine=self.space['9'])
        
        print board


    def get_available_spaces(self):
        """ Returns list of available moves """
        available_spaces = []
        for key,value in self.space.iteritems():
            if value == ' ':
                available_spaces.append(key)
        return sorted(available_spaces)

    def available_edges(self, available_spaces):
        for edge in self.edges:
            if edge not in available_spaces:
                self.edges.remove(edge)
        return self.edges
    
    def available_corners(self, available_spaces):
        for corner in self.corners:
            if corner not in available_spaces:
                self.corners.remove(corner)
        return self.corners

    def check_for_win(self, row):
        """Returns true if all player marks are the same"""
        return all(mark == row[0] for mark in row)


    def get_winner (self):
        bottom_row = [self.space['1'], self.space['2'], self.space['3']]
        middle_row = [self.space['4'], self.space['5'], self.space['6']]
        top_row = [self.space['7'], self.space['8'], self.space['9']]
        left_column = [self.space['7'], self.space['4'], self.space['1']]
        middle_column = [self.space['8'], self.space['5'], self.space['2']]
        right_column = [self.space['9'], self.space['6'], self.space['3']]
        left_diagonal = [self.space['7'], self.space['5'], self.space['3']]
        right_diagonal = [self.space['9'], self.space['5'], self.space['1']]
        
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

class Player(object):

    def __init__(self):
        self.player_mark = 'X'


    def player_mark(self):
        return self.player_mark


    def move(self, available_spaces):
        move = ''

        if self.is_first_move(available_spaces):
            print "\nMake your first move...\nYou will be 'X'"
            while not self.is_move_valid(move, available_spaces):
                move = raw_input("\nWhere would you like to go first?\nEnter a number (1-9) >> ")
                if move in available_spaces:
                    return move
        else:
            while not self.is_move_valid(move, available_spaces):
                move = raw_input("\nWhere would you like to go next?\nChoose from the following: {0}>> " .format(available_spaces))
                if move in available_spaces:
                    return move


    def is_first_move(self, available_spaces):
        return len(available_spaces) == 9


    def is_move_valid(self, selection, available_spaces):
        """ Returns true if player selects an available space. Else false. """
        return selection in available_spaces


