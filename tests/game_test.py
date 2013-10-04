from unittest import TestCase, main

from src.tic_tac_toe import Board, Player
import game

class TestTicTacToe(TestCase):
    
    def setUp(self):
        TestCase.setUp(self)
        self.b = Board()
        self.p = Player()
        self.game = game

    def test_counter_first_move_center(self):
        move = game.counter_first_move('4', self.b.center, self.b.corners)
        self.assertEqual(move, '5', "Should be '5'")

    def test_counter_first_move_corner(self):
        move = game.counter_first_move('5', self.b.center, self.b.corners)
        self.assertTrue(move in self.b.corners, "Should be a corner")

    def test_counter_first_move_edger(self):
        move = game.counter_second_move('4', self.b.edges, self.b.corners)
        self.assertTrue(move in self.b.edges, "Should be an edge")

    def test_counter_second_move_corner(self):
        move = game.counter_second_move('7', self.b.edges, self.b.corners)
        self.assertTrue(move in self.b.corners, "Should be a corner")

    def test_computer_move_none(self):
        move = game.computer_move([])
        self.assertEqual(move, None, "Should be None")

    def test_computer_move(self):
        move = game.computer_move(self.b.available_spaces())
        self.assertTrue(move in self.b.available_spaces(), 
                        "Should be one of {0}".format(self.b.available_spaces()))

    def test_prevent_win(self):
        self.b.spaces['1'] = self.p.player_mark
        self.b.spaces['2'] = self.p.player_mark
        self.b.spaces['3'] = ' '
        space = game.prevent_win(self.b.spaces, self.p.player_mark, self.b.possible_wins)
        self.assertEqual(space, '3', "Space to update should be '3'")

    def test_prevent_win_none(self):
        self.b.spaces['1'] = self.p.player_mark
        self.b.spaces['2'] = ' '
        self.b.spaces['3'] = ' '
        space = game.prevent_win(self.b.spaces, self.p.player_mark, self.b.possible_wins)
        self.assertEqual(space, None, "Space to update should be None")

    def test_go_for_win(self):
        self.b.spaces['1'] = self.b.computer_mark
        self.b.spaces['5'] = self.b.computer_mark
        self.b.spaces['9'] = ' '
        space = game.go_for_win(self.b.spaces, self.b.computer_mark, self.b.possible_wins)
        self.assertEqual(space, '9', "Space to update should be '9'")

    def test_go_for_win_none(self):
        self.b.spaces['1'] = ' '
        self.b.spaces['5'] = self.b.computer_mark
        self.b.spaces['9'] = ' '
        space = game.go_for_win(self.b.spaces, self.b.computer_mark, self.b.possible_wins)
        self.assertEqual(space, None, "Space to update should be None")

    def tearDown(self):
        TestCase.tearDown(self)
        
if __name__ == '__main__':
    main()