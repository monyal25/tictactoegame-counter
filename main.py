"""
Tic-Tac-Toe Game State Generator

This program generates all possible tic-tac-toe games following proper rules
and counts unique valid completed game states.

Rules:
- X always goes first
- Players alternate turns
- Game ends when someone wins or board is full (tie)
- Only count unique end states (no duplicates)
"""

class TicTacToeGenerator:
    def __init__(self):
        # Set to store unique completed game states
        self.completed_states = set()
        # Counter for total games explored
        self.games_explored = 0

    def create_empty_board(self):
        """Create an empty 3x3 tic-tac-toe board"""
        return [' ' for _ in range(9)]

    def board_to_tuple(self, board):
        """Convert board list to tuple for hashing"""
        return tuple(board)

    def print_board(self, board):
        """Print board in a readable format (for debugging)"""
        for i in range(0, 9, 3):
            print(f" {board[i]} | {board[i+1]} | {board[i+2]} ")
            if i < 6:
                print("-----------")

    def check_winner(self, board):
        """
        Check if there's a winner on the board
        Returns 'X', 'O', or None
        """
        # All possible winning combinations (rows, columns, diagonals)
        winning_positions = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
            [0, 4, 8], [2, 4, 6]              # diagonals
        ]

        for positions in winning_positions:
            if (board[positions[0]] == board[positions[1]] == board[positions[2]]
                and board[positions[0]] != ' '):
                return board[positions[0]]

        return None

    def is_board_full(self, board):
        """Check if the board is completely filled"""
        return ' ' not in board

    def is_game_complete(self, board):
        """
        Check if game is complete (someone won or it's a tie)
        Returns (is_complete, winner_or_tie)
        """
        winner = self.check_winner(board)
        if winner:
            return True, winner
        elif self.is_board_full(board):
            return True, 'tie'
        else:
            return False, None

    def get_available_moves(self, board):
        """Get list of available positions (empty spaces)"""
        return [i for i in range(9) if board[i] == ' ']

    def generate_all_games(self, board=None, is_x_turn=True):
        """
        Recursively generate all possible tic-tac-toe games

        Args:
            board: Current board state (list of 9 elements)
            is_x_turn: True if it's X's turn, False if it's O's turn
        """
        # Initialize with empty board on first call
        if board is None:
            board = self.create_empty_board()

        # Check if current game state is complete
        is_complete, result = self.is_game_complete(board)

        if is_complete:
            # Game is finished, add to our set of completed states
            state_tuple = self.board_to_tuple(board)
            self.completed_states.add(state_tuple)
            self.games_explored += 1
            return

        # Get all available moves
        available_moves = self.get_available_moves(board)

        # Current player symbol
        current_player = 'X' if is_x_turn else 'O'

        # Try each possible move
        for move in available_moves:
            # Make a copy of the board for this branch
            new_board = board.copy()
            new_board[move] = current_player

            # Recursively explore this game path with the other player's turn
            self.generate_all_games(new_board, not is_x_turn)

    def count_unique_completed_games(self):
        """
        Generate all possible games and return count of unique completed states
        """
        print("Generating all possible tic-tac-toe games...")

        # Start the recursive generation
        self.generate_all_games()

        return len(self.completed_states)

    def analyze_results(self):
        """Analyze and display detailed results"""
        print(f"\nAnalysis Results:")
        print(f"Total games explored: {self.games_explored}")
        print(f"Unique completed game states: {len(self.completed_states)}")

        # Count different types of endings
        x_wins = 0
        o_wins = 0
        ties = 0

        for state in self.completed_states:
            winner = self.check_winner(list(state))
            if winner == 'X':
                x_wins += 1
            elif winner == 'O':
                o_wins += 1
            else:
                ties += 1

        print(f"\nBreakdown of completed games:")
        print(f"X wins: {x_wins}")
        print(f"O wins: {o_wins}")
        print(f"Ties: {ties}")

        return len(self.completed_states)

def main():
    """Main function to run the tic-tac-toe game generator"""
    print("Tic-Tac-Toe Game State Generator")
    print("Generating all possible valid, completed tic-tac-toe games...")
    print("Rules: X goes first, players alternate, counting unique end states only")
    print()

    # Create generator instance
    generator = TicTacToeGenerator()

    # Generate all games and count unique completed states
    unique_count = generator.count_unique_completed_games()

    # Display results
    generator.analyze_results()

    print(f"FINAL ANSWER: {unique_count} unique valid completed game states")

if __name__ == "__main__":
    main()
