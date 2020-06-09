# class gives particulars about each vehicle object
lass Vehicle:
    """
    This class represents a vehicle in a game of rush hour.

    Args:
        name: String representing the name for the vehicle.
        size: Integer representing the length of the vehicle.
        position: List tuples containing integers. The list represents the position of the vehicle on the board.
        orientation: String that indicates the direction of the vehicle.
    """

    def __init__(self, id, size, position, orientation):
        self.id = id
        self.size = size
        self.position = position
        self.orientation = orientation

    def __str__(self):
        return 'Vehicle object:'str(self.id) + ' of size ' + str(self.size) + ' positioned on gridboxes ' +
         str(self.position) + ' has a ' + str(self.orientation) + ' orientation.'

    def move()
