# Utilities


def get_enclosed_boxes(box_1, box_2):
    """
    Gets the boxes that are enclosed between box_1 and box_2, where a box is defined as a pair of coordinates
    representing a location on a 2D grid. box_1 and box_2 must be either in the same column or in the same row.
    Args:
        box_1: Tuple of integers (i, j) representing the location of the first box.
        box_2: Tuple of integers (i, j) representing the location of the second box.
    Returns:
        List of tuples containing integers [(i_1, j_1),(i_2, j_2)] that represent the enclosed boxes between box_1 and
        box_2.
    """

    enclosed_boxes = []
    # Check if the boxes are in the same row.
    if box_1[0] == box_2[0]:
        # Remember the row that the boxes are in.
        row = box_1[0]

        # Check if box_1 is on the left of box_2.
        if box_1[1] < box_2[1]:
            enclosed_boxes_count = box_2[1] - box_1[1]
            left_most_column = box_1[1]
        else:
            enclosed_boxes_count = box_1[1] - box_2[1]
            left_most_column = box_2[1]

        # Loop over the enclosed columns.
        for i in range(1, enclosed_boxes_count):
            enclosed_box = (row, left_most_column + i)
            enclosed_boxes.append(enclosed_box)
    else:
        # Remember the column that the boxes are in.
        column = box_1[1]

        # Check if box_1 is above box_2.
        if box_1[0] < box_2[0]:
            enclosed_boxes_count = box_2[0] - box_1[0]
            upper_most_row = box_1[0]
        else:
            enclosed_boxes_count = box_1[0] - box_2[0]
            upper_most_row = box_2[0]

        # Loop over the enclosed rows.
        for i in range(1, enclosed_boxes_count):
            enclosed_box = (upper_most_row + i, column)
            enclosed_boxes.append(enclosed_box)

    return enclosed_boxes


def get_red_car(game):
    """
    Gets the red car given a game.

    Args:
        game: (type Game) Instance of a game.
    Returns:
        Vehicle (type Vehicle) representing the red car.
    """

    # Find the red car.
    red_car = None
    for vehicle in game.vehicles:
        if vehicle.id == 'X':
            red_car = vehicle
            break

    return red_car


def get_red_car(game):
    """
    Gets the red car given a game.

    Args:
        game: (type Game) Instance of a game.
    Returns:
        Vehicle (type Vehicle) representing the red car.
    """

    # Find the red car.
    red_car = None
    for vehicle in game.vehicles:
        if vehicle.id == 'X':
            red_car = vehicle
            break

    return red_car


def finish_game(game):
    """
    TODO: write docstring
    Args:
        game:

    Returns:

    """
    # game.board.finish = (i, j)
    # game.board.finish_position = [(3, 5), (3, 6)]
    # TODO: maybe make finish_position an attribute of the board class.
    game.move(game.red_car, game.board.finish_position)
