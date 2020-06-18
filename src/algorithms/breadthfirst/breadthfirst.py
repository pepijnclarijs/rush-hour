# This src was taken and altered from Bas Terwijn's constructive algorithm series on youtube.
# https://www.youtube.com/watch?v=NqSSrKDAE_U&list=PLJBtJTYGPSzIfEzXpszM8Ewsllwfa0d6T&index=9

import copy
import queue as q
import random

from src.heuristics.is_exit_reachable import is_exit_reachable
from src.heuristics.is_state_unique import is_state_unique
from src.util import finish_game


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
        # Track states
        seen_states = []

        queue = q.Queue()

        # Add begin game instance to queue.
        queue.put((game, [""]))
        seen_states.append(game.current_state)
        while not queue.empty():
            # Get first from queue.
            node = queue.get()
            current_game_instance = copy.deepcopy(node[0])
            current_depth = len(node[1])
            print(len(node[1]))

            # Don't search deeper than 'depth'.
            while current_depth < depth:
                for move in current_game_instance.possible_moves:
                    # Get the move specifics.
                    vehicle = move[0]
                    steps = move[1]
                    new_position = vehicle.speculate_new_position(steps)

                    # Execute the move if possible.
                    if current_game_instance.validate_move(vehicle, new_position):
                        current_game_instance.move(vehicle, new_position)
                        # TODO: This should not be done here, but in the game class. Make a function that calculates the steps, given a vehicle (start position)
                        # TODO: And its end position.
                        current_game_instance.update_executed_moves(move)

                        # Heuristic: Check if the state is unique.
                        if not is_state_unique(seen_states, current_game_instance.current_state):
                            continue

                        # Otherwise, remember the state.
                        seen_states.append(current_game_instance.current_state)

                        # Add new child node to queue.
                        moves_until_state = copy.deepcopy(node[1])
                        moves_until_state.append(move)
                        child_node = (current_game_instance, moves_until_state)
                        queue.put(child_node)

                        # Heuristic: check if the boxes from the red car up until the exit are free.
                        if is_exit_reachable(current_game_instance):
                            finish_game(current_game_instance)

                        if current_game_instance.is_finished():
                            break
        solved_cases[f"{i}"] = current_game_instance.executed_moves

    return solved_cases