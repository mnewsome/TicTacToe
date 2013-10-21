from unittest import TestCase, main

from src.player import Player, ComputerPlayer
from src.board import Board

class TestTicTacToe(TestCase):
    def setUp(self):
        TestCase.setUp(self)
        self.p = Player('X')
        self.c = ComputerPlayer('O')
        self.b = Board()

    #
    # - Test Human Player Object
    #
    def test_player_mark(self):
        move = self.p.mark
        self.assertEqual(move, 'X', "Player mark should be 'X'")

    def test_player_first_move(self):
        move = self.p.move(first_move=True)
        self.assertEqual(move, move, "Should return input from player")

    def test_player_subsequent_move(self):
        move = self.p.move()
        self.assertEqual(move, move, "Should return input from player")


    #
    # - Test Computer Player/AI Object
    #
    def test_computer_mark(self):
        m = self.c.mark
        self.assertEqual(m, 'O', "Computer mark should be 'X'")

    def test_counter_first_move_center(self):
        move = self.c.counter_first_move('4', self.b.center, self.b.corners)
        self.assertEqual(move, '5', "Should be '5'")

    def test_counter_first_move_corner(self):
        move = self.c.counter_first_move('5', self.b.center, self.b.corners)
        self.assertTrue(move in self.b.corners, "Should be a corner")

    def test_counter_second_move_edge(self):
        move = self.c.counter_second_move('1', '4', self.b.edges, self.b.corners, self.b.check_edges)
        self.assertTrue(move in self.b.edges, "Should be an edge")

    def test_counter_second_move_corner(self):
        move = self.c.counter_second_move('4', '7', self.b.edges, self.b.corners, self.b.check_edges)
        self.assertTrue(move in self.b.corners, "Should be a corner")

    def test_counter_second_move_two_edges(self):
        self.b.spaces['2'] = self.p.mark
        self.b.spaces['6'] = self.p.mark
        self.b.spaces['5'] = self.c.mark
        move = self.c.counter_second_move('2', '6', self.b.available_edges(), self.b.available_corners(), self.b.check_edges)
        self.assertEqual(move, '3', "Should be '3'. returned {0}".format(move))

    def test_computer_move_none(self):
        move = self.c.move([])
        self.assertEqual(move, None, "Should be None")

    def test_computer_move(self):
        move = self.c.move(self.b.available_spaces())
        self.assertTrue(move in self.b.available_spaces(), 
                        "Should be one of {0}".format(self.b.available_spaces()))

    def test_prevent_win(self):
        self.b.spaces['1'] = self.p.mark
        self.b.spaces['2'] = self.p.mark
        self.b.spaces['3'] = ' '
        space = self.c.prevent_win(self.b.spaces, self.p.mark, self.b.possible_wins)
        self.assertEqual(space, '3', "Space to update should be '3'")

    def test_prevent_win_none(self):
        self.b.spaces['1'] = self.p.mark
        self.b.spaces['2'] = ' '
        self.b.spaces['3'] = ' '
        space = self.c.prevent_win(self.b.spaces, self.p.mark, self.b.possible_wins)
        self.assertEqual(space, None, "Space to update should be None")

    def test_go_for_win(self):
        self.b.spaces['1'] = self.c.mark
        self.b.spaces['5'] = self.c.mark
        self.b.spaces['9'] = ' '
        space = self.c.go_for_win(self.b.spaces, self.c.mark, self.b.possible_wins)
        self.assertEqual(space, '9', "Space to update should be '9'")

    def test_go_for_win_none(self):
        self.b.spaces['1'] = ' '
        self.b.spaces['5'] = self.c.mark
        self.b.spaces['9'] = ' '
        space = self.c.go_for_win(self.b.spaces, self.c.mark, self.b.possible_wins)
        self.assertEqual(space, None, "Space to update should be None")
        
    def tearDown(self):
        TestCase.tearDown(self)

if __name__ == '__main__':
    main()