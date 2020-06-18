# Checks if the red car can be moved to the finish.

from src.util import get_red_car


def is_exit_reachable(game):
    """
    Checks if the red car can be moved to the finish.

    Args:
        game: Game representing the game in which we want to check if the exit is reachable.

    Returns:
        Boolean indicating if the red car is able to move to the finish.
    """

    # Find the red car.
    red_car = get_red_car(game)

    # Check if the red car can be moved to the exit.
    if game.validate_move(red_car, game.board.finish_position):
        return True

    return False
