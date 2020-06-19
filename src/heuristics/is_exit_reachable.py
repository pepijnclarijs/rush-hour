# Checks if the red car can be moved to the finish.

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
