import sys

from load import load_game, load_initial_board

# Start game
def randomize(board_size, runs):
    solved_cases = {}

    for i in range(runs):
        # Load new game
        game = load_game(board_size, initial_board)

        
        # Create a list to track the movements.
        moves = []

        # Move vehicles around randomly until the game is finished.
        tries = 0
        while not game.is_finished():
