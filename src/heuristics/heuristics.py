def is_state_unique(seen_states, state):
    """
    Checks if a state has not yet occurred in a given game.

    Args:
        seen_states (list of dict of strings and list of tuples containing ints): Represents the states that have been
            seen already.
        state (dict of strings and list of tuples containing ints): Represents a state of the game.

    Returns:
        Boolean indicating whether the state is unique or not.
    """

    if state in seen_states:
        return False

    return True

def is_exit_reachable(game):
    """
    Checks if the red car can be moved to the finish.

    Args:
        game: Game representing the game in which we want to check if the exit is reachable.

    Returns:
        Boolean indicating if the red car is able to move to the finish.
    """

    # Find the red car.
    red_car = game.red_car

    # Check if the red car can be moved to the exit.
    if game.validate_move(red_car, game.board.finish_position):
        return True

    return False    
