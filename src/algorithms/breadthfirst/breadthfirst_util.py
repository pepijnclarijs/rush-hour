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
    vehicles = {}
    for vehicle_id in state:
        vehicle = Vehicle(vehicle_id, state[vehicle_id])
        vehicles[vehicle_id] = vehicle

    game = Game(board, vehicles)

    return game
