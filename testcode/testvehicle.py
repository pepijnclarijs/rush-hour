class Vehicle:
    """
    This class represents a vehicle in a game of rush hour.

    Args:
        id: String representing the name for the vehicle.
        position: List tuples containing integers [(i_1, j_1),(i_2, j_2)]. The list represents the position of the
                    vehicle on the board.
    """
    # def __init__(self, id, position):
    #     self.id = id
    #     self.position = position
    def __init__(self, id, orientation, row, column, size):
        self.id = id
        self.orientation = orientation
        self.row = row
        self.column = column
        self.size = size
