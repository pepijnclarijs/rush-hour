# This src was taken and altered from Bas Terwijn's constructive algorithm series on youtube.
# https://www.youtube.com/watch?v=NqSSrKDAE_U&list=PLJBtJTYGPSzIfEzXpszM8Ewsllwfa0d6T&index=9

# This src was taken and altered from Bas Terwijn's constructive algorithm series on youtube.
# https://www.youtube.com/watch?v=NqSSrKDAE_U&list=PLJBtJTYGPSzIfEzXpszM8Ewsllwfa0d6T&index=9

import copy
import queue as q
import random

from load import load_game
from src.heuristics.is_exit_reachable import is_exit_reachable
from src.heuristics.is_state_unique import is_state_unique
from src.util import finish_game
from src.algorithms.breadthfirst.breadthfirst_util import create_game_from_state


def breadth_first(initial_game, runs, depth):
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
        # Track states.
        seen_states = []

        queue = q.Queue()

        # Add begin state to queue.
        initial_state = initial_game.current_state
        queue.put((initial_state, [""], 0))
        seen_states.append(initial_state)
        board_size = initial_game.board.length
        node_id = 0
        while not queue.empty():
            # Get first from queue.
            parent_node = copy.deepcopy(queue.get())
            current_depth = len(parent_node[1])
            print(current_depth)

            # Don't search deeper than 'depth'.
            if current_depth < depth:
                # Create a game instance from the state
                parent_state = parent_node[0]
                parent_game = create_game_from_state(parent_state, board_size)

                # Loop over the possible moves in the state.
                possible_moves = parent_game.possible_moves
                for move in possible_moves:
                    # Get the move specifics.
                    vehicle = move[0]
                    steps = move[1]
                    new_position = vehicle.speculate_new_position(steps)

                    # Execute the move if possible to create a child node.
                    if parent_game.validate_move(vehicle, new_position):
                        child_game = copy.deepcopy(parent_game)
                        child_vehicle = child_game.vehicles.get(vehicle.id)
                        child_game.move(child_vehicle, new_position)

                        # Heuristic: Check if the state is unique.
                        child_state = child_game.current_state
                        if not is_state_unique(seen_states, child_state):
                            continue

                        # Otherwise, remember the state.
                        seen_states.append(child_state)

                        # Add new child node to queue.
                        moves_until_state = copy.deepcopy(parent_node[1])
                        moves_until_state.append((vehicle.id, steps))
                        node_id += 1
                        child_node = (child_state, moves_until_state, node_id)
                        queue.put(child_node)

                        # Heuristic: check if the boxes from the red car up until the exit are free.
                        if is_exit_reachable(child_game):
                            last_move = finish_game(child_game)
                            moves = child_node[1]
                            moves.append(last_move)
                            solved_cases[i] = moves

                        if child_game.is_finished():
                            return solved_cases
            else:
                break

    return solved_cases


def execute_breadthfirst(initial_game, runs, depth):
    """
    Executes the breadth first algorithm.

    Args:
        initial_game (Game): The game that should be solved.
        runs (int): The number of times the game should be solved.
        depth: The depth until which the breadth first should be tried.

    Returns:
        Dict of int: dict of
    """

# Set number of runs.
runs = 1
board_size = 6
game_number = "1"

# Load game.
game = load_game(game_number, board_size)
result = breadth_first(game, runs, 22)
print(result)
