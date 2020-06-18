# TODO: The only thing we need is a "create_game_from_state" function so that we can use the functions in that game.
# TODO: def get_vehicle(id): If this function can be made, we can upgrade the nodes to holding only the vehicle id's.
from src.classes.board import Board
from src.classes.game import Game
from src.classes.vehicle import Vehicle


def create_game_from_state(state, board_size):
    """
    Creates a game instance given a state of a game and a board size.

    Args:
        state (dict of str: list of tuples of integers): Represents the state of a game.
        board_size: The size of the length/width of the board.

    Returns:
            Game instance having the given state as current state.
    """

    board = Board(board_size)

    # Create the vehicles from the state.
    vehicles = []
    for vehicle_id in state:
        vehicle = Vehicle(vehicle_id, state[vehicle_id])
        vehicles.append(vehicle)

    game = Game(board, vehicles)

    return game


def get_vehicle(id, vehicles):
    """
    Finds a vehicle in a list of vehicles given a vehicle id.

    Args:
        id (string): The id of the vehicle.
        vehicles (list of vehicles): The list of vehicles.

    Returns:
            The vehicle with the given id.
    """

    for vehicle in vehicles:
        if vehicle.id == id:
            return vehicle

    return None
