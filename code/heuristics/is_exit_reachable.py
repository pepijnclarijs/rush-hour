def is_exit_reachable(game):
    """
    Checks if the red car can be moved to the finish.

    Args:
        game: Game representing the game in which we want to check if the exit is reachable.

    Returns:
        Boolean indicating if the red car is able to move to the finish.
    """

    # Find the red car.
    for vehicle in game.vehicles:
        if vehicle.id == 'X':
            red_car = vehicle
            break

    # Check if the red car can be moved to the exit.
    if game.validate_move(red_car, game.finish):
        return True

    return False

