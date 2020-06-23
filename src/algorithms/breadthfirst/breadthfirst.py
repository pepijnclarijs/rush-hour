import copy
import queue as q

from src.heuristics.heuristics import is_exit_reachable, is_state_unique
from src.util import finish_game
from src.algorithms.breadthfirst.breadthfirst_util import create_game_from_state
from src.load import load_game


def breadthfirst(initial_game):
    """
    Uses a breadth first algorithm to solve a given game of Rush Hour.
    Args:
        initial_game (Game): Instance of the initial game.
    Returns:
        Dict of int: List of tuples containing a string representing the id of a vehicle and an integer representing the
        number of steps [('A', 2), ('B', -2)]. The list represents the movements that should be executed to solve the
        game.
    """
    # Creat dict for solved case
    solved_cases = {}

    # Track states.
    seen_states = []

    queue = q.Queue()

    # Add begin state to queue.
    initial_state = initial_game.current_state
    queue.put((initial_state, []))
    seen_states.append(initial_state)
    board_size = initial_game.board.length

    while not queue.empty():
        # Get first from queue.
        parent_node = copy.deepcopy(queue.get())

        # Create a game instance from the state
        parent_state = parent_node[0]
        parent_game = create_game_from_state(parent_state, board_size)

        # Loop over the possible moves in the state.
        possible_moves = parent_game.possible_moves
        for move in possible_moves:
            # Get the move specifics.
            vehicle, steps = move
            new_position = vehicle.speculate_new_position(steps)

            # Execute the move to create a child node.
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
            child_node = (child_state, moves_until_state)
            queue.put(child_node)

            # Heuristic: check if the boxes from the red car up until the exit are free.
            if is_exit_reachable(child_game):
                last_move = finish_game(child_game)
                moves = child_node[1]
                moves.append(last_move)
                solved_cases[0] = moves

            if child_game.is_finished():
                solved_cases

    return "No solved cases have been found :("
