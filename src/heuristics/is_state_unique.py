# Checks if a given state is unique given a game.


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
