import copy

from src.heuristics.heuristics import is_exit_reachable
from src.util import finish_game
from src.algorithms.breadthfirst.breadthfirst_util import create_game_from_state


def breachbound(initial_game, max_depth):
    """
    Uses a breadth first algorithm to solve a given game of Rush Hour.
    Args:
        initial_game (Game): The instance of the initial game.
        max_depth (int): The depth up until which should be searched.
    Returns:
        List of tuples containing a string representing the id of a vehicle and an integer representing the number of
        steps [('A', 2), ('B', -2)]. The list represents the movements that should be executed to solve the game.
    """
    # Create dict for solved case
    solved_cases = {}

    # Track nodes
    seen_nodes = []

    # Add initial node to the stack.
    initial_state = initial_game.current_state
    moves_until_state = []
    initial_node = (initial_state, moves_until_state)
    stack = [initial_node]
    seen_nodes.append(initial_node)
    board_size = initial_game.board.length

    while len(stack) > 0:
        print(f"Number of passed nodes is: {len(seen_nodes)}")

        # Get first from queue.
        parent_node = stack.pop()

        # Check current depth.
        moves_until_state = parent_node[1]
        current_depth = len(moves_until_state)
        if current_depth < max_depth:
            # Create a game instance from the state.
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
                child_state = child_game.current_state
                moves_until_state = copy.deepcopy(parent_node[1])
                moves_until_state.append((vehicle.id, steps))
                child_node = (child_state, moves_until_state)

                # Heuristic: Check if the route to the state is the shortest so far.
                if not is_shortest_route_to_state(seen_nodes, child_node):
                    continue

                # If it is, remember the state.
                seen_nodes.append(child_node)

                # Add new child node to the stack.
                stack.append(child_node)

                # Heuristic: check if the boxes from the red car up until the exit are free.
                if is_exit_reachable(child_game):
                    last_move = finish_game(child_game)
                    moves = child_node[1]
                    moves.append(last_move)
                    solved_cases[0] = moves

    # Get the best solution.
    previous_case = 999999999
    for case in solved_cases:
        moves = solved_cases[case]
        moves_count = len(moves)
        if moves_count < previous_case:
            previous_case = moves_count
            best_solution = moves
    return_result = {0: best_solution}
    return return_result


def is_shortest_route_to_state(seen_nodes, node):
    """
    Checks if a given state was reached with the shortest route possible.

    Args:
        seen_nodes (list of tuple of dict of str: list of tuple of int, list of tuple of str, int): The nodes that have
                have been seen so far.
        node ((state, moves)): Represents a point in a tree of states.

    Returns:
        Boolean representing if the given route to the given state is the shortest so far.
    """

    given_state, given_moves = node

    if len(seen_nodes) < 1:
        return True

    for node in seen_nodes:
        state, moves = node
        if state == given_state:
            if len(moves) < len(given_moves):
                return False

    return True

