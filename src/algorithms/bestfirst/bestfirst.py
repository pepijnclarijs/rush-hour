import copy
import queue as q

from src.heuristics.heuristics import is_exit_reachable, is_state_unique
from src.util import finish_game
from src.algorithms.breadthfirst.breadthfirst_util import create_game_from_state


def bestfirst(initial_game, exit_reachable, state_unique, winning_state, max_tries):
    """
    Uses a best first algorithm to solve a given game of Rush Hour.
    Args:
        initial_game (Game): Instance of the initial game.
        winning_state (dict of str: list of tuple of int, int): The state of a board that is finished.
    Returns:
        Dict of int: List of tuples containing a string representing the id of a vehicle and an integer representing the
        number of steps [('A', 2), ('B', -2)]. The list represents the movements that should be executed to solve the
        game.
    """

    # Create dict for solved case.
    solved_cases = {}

    # Track states.
    seen_states = []

    # Create priority queue.
    queue = q.PriorityQueue()

    # Get initial state, give it a heuristic value and add to queue.
    initial_state = initial_game.current_state
    heuristic = calc_heuristic(initial_state, winning_state)
    queue.put((heuristic, [], initial_state))
    seen_states.append(initial_state)
    board_size = initial_game.board.length
    case_number = 0
    moves_to_win = []
    while not queue.empty():
        # Get first from queue.
        parent_node = copy.deepcopy(queue.get())

        # Create a game instance from the state
        parent_state = parent_node[2]
        parent_game = create_game_from_state(parent_state, board_size)

        # Skip states that are already finished.
        if parent_game.is_finished():
            continue

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

            child_state = child_game.current_state
            if state_unique:
                # Heuristic: Check if the state is unique.
                if not is_state_unique(seen_states, child_state):
                    continue

            # Otherwise, remember the state.
            seen_states.append(child_state)

            # Add new child node to queue.
            moves_until_state = copy.deepcopy(parent_node[1])
            moves_until_state.append((vehicle.id, steps))
            child_heuristic = calc_heuristic(child_state, winning_state)
            child_node = (child_heuristic, moves_until_state, child_state)
            queue.put(child_node)

            if exit_reachable:
                # Heuristic: check if the boxes from the red car up until the exit are free.
                if is_exit_reachable(child_game):
                    last_move = finish_game(child_game)
                    moves_to_win = child_node[1]
                    moves_to_win.append(last_move)

            if child_game.is_finished():
                if len(moves_to_win) > 0:
                    solved_cases[case_number] = moves_to_win
                    print(f"Solved cases: {len(solved_cases)}")
                    moves_to_win = []
                else:
                    solved_cases[case_number] = child_node[1]
                    print(f"Solved cases: {len(solved_cases)}")

                case_number += 1

            if max_tries > 0:
                if case_number >= max_tries:
                    return solved_cases

    if len(solved_cases.values()) > 0:
        return solved_cases

    return {0: "No solved cases have been found :("}


def calc_heuristic(state, winning_state):
    """
    Gives a heuristic value to a state, indicating the how close it is to finishing the game. The heuristic value is
    based on the number of vehicles that are in the same position as they are in the winning_state, and the number of
    vehicles in the game. The lower the heuristic value, the more chance the state is thought to have to finish in the
    shortest number of moves.

    Args:
        state (dict of str: list of tuples of int, int): The current state of the game.
        winning_state (dict of str: list of tuples of int, int): The state that the game is in when it is finished.

    Returns:
            int: The heuristic value given to the state.
    """

    vehicle_count = len(state)

    # Check the shared key-value pairs.
    shared_items = {k: state[k] for k in state if k in winning_state and state[k] == winning_state[k]}
    correct_vehicle_count = len(shared_items)

    return vehicle_count - correct_vehicle_count


