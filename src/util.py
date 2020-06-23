# Utilities
from src.classes.board import Board
from src.classes.game import Game
from src.classes.vehicle import Vehicle


def get_enclosed_boxes(box_1, box_2):
    """
    Gets the boxes that are enclosed between box_1 and box_2, where a box is defined as a pair of coordinates
    representing a location on a 2D grid. box_1 and box_2 must be either in the same column or in the same row.
    Args:
        box_1 (Tuple of ints): (i, j) representing the location of the first box.
        box_2 (Tuple of ints): (i, j) representing the location of the second box.
    Returns:
        List of tuples containing integers [(i_1, j_1),(i_2, j_2)] that represent the enclosed boxes between box_1 and
        box_2.
    """

    enclosed_boxes = []

    # Get the specifics.
    row_1, col_1 = box_1
    row_2, col_2 = box_2

    # Check if the boxes are in the same row.
    if row_1 == row_2:
        # Remember the row that the boxes are in.
        row = row_1

        # Check if box_1 is on the left of box_2.
        if col_1 < col_2:
            enclosed_boxes_count = col_2 - col_1
            left_most_column = col_1
        else:
            enclosed_boxes_count = col_1 - col_2
            left_most_column = col_2

        # Loop over the enclosed columns.
        for i in range(1, enclosed_boxes_count):
            enclosed_box = (row, left_most_column + i)
            enclosed_boxes.append(enclosed_box)
    else:
        # Remember the column that the boxes are in.   box_1[0] = row_1, box_1[1] = col_1
        column = col_1

        # Check if box_1 is above box_2.
        if row_1 < row_2:
            enclosed_boxes_count = row_2 - row_1
            upper_most_row = row_1
        else:
            enclosed_boxes_count = row_1 - row_2
            upper_most_row = row_2

        # Loop over the enclosed rows.
        for i in range(1, enclosed_boxes_count):
            enclosed_box = (upper_most_row + i, column)
            enclosed_boxes.append(enclosed_box)

    return enclosed_boxes


def finish_game(game):
    """
    Finishes the game by moving the red car to the end position.

    Args:
        game (Game): The game that should be finished.

    Returns:
        The last move that is done to finish the game.
    """

    red_car = game.red_car

    # Calculate the steps the red car has to do.
    if red_car.position[0][1] > red_car.position[-1][1]:
        right_most_box = red_car.position[0]
    else:
        right_most_box = red_car.position[-1]

    steps = game.board.finish_box[1] - right_most_box[1]
    last_move = (game.red_car.id, steps)

    game.move(red_car, game.board.finish_position)

    return last_move


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
