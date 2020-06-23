import copy, random

from src.heuristics.heuristics import is_exit_reachable, is_state_unique
from src.util import finish_game
from src.load import load_game


def depthfirstbbr2(parent_node):
    """
    Uses a branch and bound algorithm to solve a given game of Rush Hour.
    Args:
        parent_node (Game): Instance of the initial game.
    Returns:
        Dict of int: List of tuples containing a string representing the id of a vehicle and an integer representing the
        number of steps [('A', 2), ('B', -2)]. The list represents the movements that should be executed to solve the
        game.
    """
    # Creat dict for solved case
    solved_cases = {}

    # moet inf zijn
    best_sol_count = 100000
    best_sol = {}
    seen_states = []
    stack = []

    stack.append(parent_node)
    seen_states.append(parent_node)

    while len(stack)>0:    
        # Get first from stack.
        state = stack.pop()

        if len(state.moves) < best_sol_count:   
            # Randomize outcome
            ps_move = list(state.possible_moves)
            random.shuffle(ps_move)

            # Create all children notes
            for move in ps_move:
                child_game = copy.deepcopy(state)

                # Get the move specifics.
                vehicle, steps = move

                new_position = vehicle.speculate_new_position(steps)

                # Move the vehicle to the new position.
                child_game.move(child_game.vehicles[vehicle.id], new_position)

                # Heuristic: Check if the state is unique.
                child_state = child_game.current_state
                if not is_state_unique(seen_states, child_state):
                    continue

                # Save the movements of the vehicles.
                moved = (vehicle.id, steps)
                child_game.moves.append(moved)
                child_game.update_possible_moves()             
                seen_states.append(child_game)
                stack.append(child_game)

                # Heuristic: check if the boxes from the red car up until the exit are free.
                if is_exit_reachable(child_game):
                    last_move = finish_game(child_game)
                    moved = (vehicle.id, steps)
                    child_game.moves.append(moved)  
                    best_sol[0] = child_game.moves

                if child_game.is_finished():
                    best_sol_count = len(child_game.moves)
                    
    return best_sol