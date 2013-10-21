from unittest import TestCase, main

from src.board import Board

class TestTicTacToe(TestCase):
    
    def setUp(self):
        TestCase.setUp(self)
        self.b = Board()

    def test_update(self):
        update = self.b.update('5', 'X')
        self.assertEqual(self.b.spaces['5'], 'X',  "Space '5' should be X")
        
    def test_available_spaces(self):
        self.b.spaces['5'] = 'O'
        self.b.spaces['9'] = 'X'
        spaces = self.b.available_spaces()
        self.assertEqual(spaces, ['1','2','3','4','6','7', '8'], 
                         "Avalaible spaces incorrect. Returned {0}".format(spaces))

    def test_get_available_edges(self):
        self.b.spaces['2'] = 'O'
        self.b.spaces['4'] = 'X'
        edges = self.b.available_edges()
        self.assertEqual(edges, ['6','8'], 
                         "Avalaible edges incorrect. Returned {0}".format(edges))

    def test_get_available_corners(self):
        self.b.spaces['7'] = 'O'
        self.b.spaces['9'] = 'X'
        corners = self.b.available_corners()
        self.assertEqual(corners, ['1','3'], 
                         "Avalaible corners incorrect. Returned {0}".format(corners))

    def test_check_for_win(self):
        check = self.b.check_for_win(['X', 'X', 'X'] )
        self.assertTrue(check, "Should be true")

    def test_check_for_win_false(self):
        check = self.b.check_for_win(['X', 'X', ''])
        self.assertFalse(check, "Should be false")

    def test_get_winner(self):
        self.b.spaces['1'] = 'X'
        self.b.spaces['2'] = 'X'
        self.b.spaces['3'] = 'X'
        winner = self.b.get_winner()
        self.assertEqual(winner, 'X', "Winner should be 'X'")
    
    def test_get_winner_none(self):
        self.b.spaces['1'] = 'X'
        self.b.spaces['2'] = 'X'
        self.b.spaces['3'] = ''
        winner = self.b.get_winner()
        self.assertEqual(winner, None, "Winner should be 'None'")

    def test_is_first_move(self):
        fm = self.b.is_first_move(self.b.available_spaces())
        self.assertTrue(fm, "Should be true")
        
    def test_is_first_move_false(self):
        self.b.spaces['1'] = 'X'
        fm = self.b.is_first_move(self.b.available_spaces())
        self.assertFalse(fm, "Should be false")

    def test_is_move_valid(self):
        self.b.spaces['1'] = 'X'
        self.b.spaces['2'] = 'X'
        vm = self.b.is_move_valid('3', self.b.available_spaces())
        self.assertTrue(vm, 'Should be true')
        
    def test_is_move_valid_false(self):
        self.b.spaces['1'] = 'X'
        self.b.spaces['2'] = 'X'
        vm = self.b.is_move_valid('2', self.b.available_spaces())
        self.assertFalse(vm, 'Should be false')
        
if __name__ == '__main__':
    main()