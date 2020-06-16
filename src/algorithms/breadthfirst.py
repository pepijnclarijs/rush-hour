# This src was taken and altered from Bas Terwijn's constructive algorithm series on youtube.
# https://www.youtube.com/watch?v=NqSSrKDAE_U&list=PLJBtJTYGPSzIfEzXpszM8Ewsllwfa0d6T&index=9

import copy
import queue as q
import random

from load import load_game


def breadth_first(game, runs, depth):
    """
    Uses a breadth first algorithm to solve a given game of Rush Hour.

    Args:
        board_size: Integer that represents the length and width of the board.
        runs: Integer that indicates the number of times the game should be solved.

    Returns:
        List of tuples containing a string representing the id of a vehicle and an integer representing the number of
        steps [('A', 2), ('B', -2)]. The list represents the movements that should be executed to solve the game.
    """

    # Solve the game 'runs' times.
    solved_cases = {}
    for i in range(runs):
        # Load new game
        # initial_board = 'data/InitialBoards/Rushhour#1.csv'
        # game = load_game(board_size, initial_board)

        # Create a list to track the movements.
        moves = []

        queue = q.Queue()

        # Add begin state to queue.
        queue.put([game.current_state])
        current_depth = 0
        while not queue.empty():
            # Get first from queue.
            state = queue.get()
            print(current_depth)

            # Don't search deeper than 'depth'.
            if current_depth < depth:
                for move in game.possible_moves:
                    # Deepcopy the state.
                    child = copy.deepcopy(state)

                    # Get the move specifics.
                    vehicle = move[0]
                    steps = move[1]
                    new_position = vehicle.speculate_new_position(steps)

                    # Execute the move.
                    game.move(vehicle, new_position)

                    # Add new child to queue.
                    new_state = game.current_state
                    child.extend(new_state)
                    queue.put(child)

                    if game.is_finished():
                        break
                else:
                    # Go to the next layer.
                    current_depth += 1
                    continue
                break
            else:
                break


        solved_cases[f"{i}"] = moves

    return solved_cases


# Set number of runs.
runs = 1
board_size = 6
game_number = "1"

# Load game.
game = load_game(game_number, board_size)
result = breadth_first(game, runs, 40)
print(result)
print(len(result['0']))

