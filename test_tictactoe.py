"""
Test cases for Tic-Tac-Toe Game State Generator

This module contains comprehensive tests for the TicTacToeGenerator class
to ensure all functionality works correctly.
"""

import unittest
from main import TicTacToeGenerator


class TestTicTacToeGenerator(unittest.TestCase):
    """Test cases for TicTacToeGenerator class"""

    def setUp(self):
        """Set up test fixtures before each test method"""
        self.generator = TicTacToeGenerator()

    def test_create_empty_board(self):
        """Test that empty board is created correctly"""
        board = self.generator.create_empty_board()
        self.assertEqual(len(board), 9)
        self.assertTrue(all(cell == ' ' for cell in board))

    def test_board_to_tuple(self):
        """Test board to tuple conversion"""
        board = ['X', 'O', ' ', 'X', 'O', ' ', 'X', 'O', ' ']
        result = self.generator.board_to_tuple(board)
        expected = ('X', 'O', ' ', 'X', 'O', ' ', 'X', 'O', ' ')
        self.assertEqual(result, expected)
        self.assertIsInstance(result, tuple)

    def test_check_winner_rows(self):
        """Test winner detection for rows"""
        # Test X winning in top row
        board = ['X', 'X', 'X', 'O', 'O', ' ', ' ', ' ', ' ']
        self.assertEqual(self.generator.check_winner(board), 'X')

        # Test O winning in middle row
        board = ['X', 'X', ' ', 'O', 'O', 'O', ' ', ' ', 'X']
        self.assertEqual(self.generator.check_winner(board), 'O')

        # Test X winning in bottom row
        board = ['O', 'O', ' ', ' ', ' ', ' ', 'X', 'X', 'X']
        self.assertEqual(self.generator.check_winner(board), 'X')

    def test_check_winner_columns(self):
        """Test winner detection for columns"""
        # Test X winning in left column
        board = ['X', 'O', 'O', 'X', ' ', ' ', 'X', ' ', ' ']
        self.assertEqual(self.generator.check_winner(board), 'X')

        # Test O winning in middle column
        board = ['X', 'O', 'X', ' ', 'O', ' ', ' ', 'O', 'X']
        self.assertEqual(self.generator.check_winner(board), 'O')

        # Test X winning in right column
        board = ['O', 'O', 'X', ' ', ' ', 'X', ' ', ' ', 'X']
        self.assertEqual(self.generator.check_winner(board), 'X')

    def test_check_winner_diagonals(self):
        """Test winner detection for diagonals"""
        # Test X winning in main diagonal (top-left to bottom-right)
        board = ['X', 'O', 'O', ' ', 'X', ' ', ' ', ' ', 'X']
        self.assertEqual(self.generator.check_winner(board), 'X')

        # Test O winning in anti-diagonal (top-right to bottom-left)
        board = ['X', 'X', 'O', ' ', 'O', ' ', 'O', ' ', 'X']
        self.assertEqual(self.generator.check_winner(board), 'O')

    def test_check_winner_no_winner(self):
        """Test when there's no winner"""
        board = ['X', 'O', 'X', 'O', 'X', 'O', 'O', 'X', 'O']
        self.assertIsNone(self.generator.check_winner(board))

        # Empty board
        board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
        self.assertIsNone(self.generator.check_winner(board))

    def test_is_board_full(self):
        """Test board full detection"""
        # Full board
        board = ['X', 'O', 'X', 'O', 'X', 'O', 'O', 'X', 'O']
        self.assertTrue(self.generator.is_board_full(board))

        # Partially filled board
        board = ['X', 'O', ' ', 'O', 'X', ' ', ' ', ' ', ' ']
        self.assertFalse(self.generator.is_board_full(board))

        # Empty board
        board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
        self.assertFalse(self.generator.is_board_full(board))

    def test_is_game_complete_winner(self):
        """Test game completion detection when there's a winner"""
        # X wins
        board = ['X', 'X', 'X', 'O', 'O', ' ', ' ', ' ', ' ']
        is_complete, result = self.generator.is_game_complete(board)
        self.assertTrue(is_complete)
        self.assertEqual(result, 'X')

        # O wins
        board = ['X', 'X', ' ', 'O', 'O', 'O', ' ', ' ', 'X']
        is_complete, result = self.generator.is_game_complete(board)
        self.assertTrue(is_complete)
        self.assertEqual(result, 'O')

    def test_is_game_complete_tie(self):
        """Test game completion detection for tie"""
        board = ['X', 'O', 'X', 'O', 'X', 'O', 'O', 'X', 'O']
        is_complete, result = self.generator.is_game_complete(board)
        self.assertTrue(is_complete)
        self.assertEqual(result, 'tie')

    def test_is_game_complete_ongoing(self):
        """Test game completion detection for ongoing game"""
        board = ['X', 'O', ' ', 'O', 'X', ' ', ' ', ' ', ' ']
        is_complete, result = self.generator.is_game_complete(board)
        self.assertFalse(is_complete)
        self.assertIsNone(result)

    def test_get_available_moves(self):
        """Test getting available moves"""
        # Partially filled board
        board = ['X', 'O', ' ', 'O', 'X', ' ', ' ', ' ', ' ']
        available = self.generator.get_available_moves(board)
        expected = [2, 5, 6, 7, 8]
        self.assertEqual(available, expected)

        # Empty board
        board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
        available = self.generator.get_available_moves(board)
        expected = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        self.assertEqual(available, expected)

        # Full board
        board = ['X', 'O', 'X', 'O', 'X', 'O', 'O', 'X', 'O']
        available = self.generator.get_available_moves(board)
        self.assertEqual(available, [])

    def test_specific_game_scenario(self):
        """Test a specific game scenario step by step"""
        # Start with empty board
        board = self.generator.create_empty_board()

        # X moves to center
        board[4] = 'X'
        self.assertFalse(self.generator.is_game_complete(board)[0])

        # O moves to corner
        board[0] = 'O'
        self.assertFalse(self.generator.is_game_complete(board)[0])

        # X moves to top-right corner
        board[2] = 'X'
        self.assertFalse(self.generator.is_game_complete(board)[0])

        # O moves to block diagonal
        board[8] = 'O'
        self.assertFalse(self.generator.is_game_complete(board)[0])

        # X moves to complete anti-diagonal win (positions 2, 4, 6)
        board[6] = 'X'
        # X should win now (anti-diagonal: positions 2, 4, 6)
        is_complete, result = self.generator.is_game_complete(board)
        self.assertTrue(is_complete)
        self.assertEqual(result, 'X')

    def test_count_unique_completed_games_small_scenario(self):
        """Test counting on a simpler scenario to verify logic"""
        # Reset the generator for clean test
        test_generator = TicTacToeGenerator()

        # Test with a board that's almost complete to limit the search space
        # This creates a scenario where there are only a few possible outcomes
        almost_complete_board = ['X', 'O', 'X', 'O', 'X', 'O', 'O', ' ', ' ']

        # Count games from this state
        test_generator.generate_all_games(almost_complete_board, False)  # O's turn

        # Should have explored some games
        self.assertGreater(test_generator.games_explored, 0)
        self.assertGreater(len(test_generator.completed_states), 0)

    def test_final_result_consistency(self):
        """Test that the final result is consistent and reasonable"""
        # Create a fresh generator
        test_generator = TicTacToeGenerator()
        unique_count = test_generator.count_unique_completed_games()

        # Verify reasonable bounds (tic-tac-toe has finite states)
        self.assertGreater(unique_count, 0)
        self.assertLess(unique_count, 10000)  # Reasonable upper bound

        # Verify that total games explored is greater than unique states
        # (because multiple game sequences can lead to same end state)
        self.assertGreater(test_generator.games_explored, unique_count)

        # Verify all completed states are actually complete
        for state in test_generator.completed_states:
            board = list(state)
            is_complete, _ = test_generator.is_game_complete(board)
            self.assertTrue(is_complete, f"State {state} should be complete")

    def test_x_always_goes_first_constraint(self):
        """Test that X always goes first constraint is maintained"""
        # Check that in any valid end state, the number of X's is either
        # equal to O's (if O made the last move) or one more than O's (if X made the last move)
        test_generator = TicTacToeGenerator()
        test_generator.count_unique_completed_games()

        for state in test_generator.completed_states:
            x_count = state.count('X')
            o_count = state.count('O')

            # X goes first, so X count should be either equal to O or one more
            self.assertTrue(
                x_count == o_count or x_count == o_count + 1,
                f"Invalid move count: X={x_count}, O={o_count} in state {state}"
            )


class TestEdgeCases(unittest.TestCase):
    """Test edge cases and boundary conditions"""

    def setUp(self):
        self.generator = TicTacToeGenerator()

    def test_immediate_win_scenarios(self):
        """Test scenarios where game ends immediately"""
        # X wins in first possible opportunity (3 moves)
        board = ['X', 'X', ' ', 'O', 'O', ' ', ' ', ' ', ' ']
        # X can win by moving to position 2
        new_board = board.copy()
        new_board[2] = 'X'

        is_complete, result = self.generator.is_game_complete(new_board)
        self.assertTrue(is_complete)
        self.assertEqual(result, 'X')

    def test_blocking_scenarios(self):
        """Test scenarios requiring blocking moves"""
        # O must block X from winning
        board = ['X', 'X', ' ', 'O', ' ', ' ', ' ', ' ', ' ']
        # O should block at position 2 to prevent X win
        available_moves = self.generator.get_available_moves(board)
        self.assertIn(2, available_moves)


if __name__ == '__main__':
    # Run all tests
    print("Running Tic-Tac-Toe Generator Test Suite")

    unittest.main(verbosity=2)
