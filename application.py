# Start solving Rush Hour here
class Game:
    """
    This class represents a game of rush hour.

    Args:
        board: This is an instance of an empty game board.
        vehicles: This is a list containing the vehicles present in the game.
    """
    def __init__ (self, board, vehicles):
        self.board = board
        self.vehicles = vehicles

    def description(self):
        return str(f'{self.board} contains: {self.vehicles}.')

    def finished(self):
        """
        Returns:
            Boolean Indicating whether the game is won or not.
        """
        # TODO: write this function

    def move(self):
        """
        Moves a vehicle on the board.

        Returns:
            Boolean indicating whether the game is won or not.
        """
        # TODO: write this function

class Board:
    """
    This class represents an empty board in a game of rush hour.

    Args:
        length: Integer representing the length of the board.
    """
    def __init__(self, length):
        # TODO: create a grid that contains a value that represents an empty spot.


class Vehicle:
    """
    This class represents a vehicle in a game of rush hour.

    Args:
        name: String representing the name for the vehicle.
        length: Integer representing the length of the vehicle.
        coordinates: List containing integers representing the coordinates on the game board that the vehicle occupies.
    """
    def __init__(self, name, size, coordinates):
        self.name = name
        self.size = size
        self.coordinates = coordinates

    def description(self):
        """
        Returns:
             String containing the name, size and coordinates of the vehicle.
        """
        # TODO: create this function
