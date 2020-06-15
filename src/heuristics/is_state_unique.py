# Checks if a given state is unique given a game.


def is_state_unique(game, state):
    """
    Checks if a state has not yet occurred in a given game.

    Args:
        game (Game): Represents the game in which it is checked if the exit is reachable.
        state (dict of strings and list of tuples containing ints): Represents a state of the game.

    Returns:
        Boolean indicating whether the state is unique or not.
    """

    if state in game.states:
        return False

    return True
