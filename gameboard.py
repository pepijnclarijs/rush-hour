# Start solving Rush Hour here
class GameBoard:
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
        Win-condition:
            Er zijn géén bezette vakjes tussen de 'getaway_car' en de uitgang,
            zodat deze in één move het 'board' kan verlaten.   ¿def won()?
        """
        # TODO: write this function

    def move(self):
        """
        Moves a vehicle on the board.

        Returns:
            Boolean indicating whether the game is won or not.
        """
        # TODO: write this function



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
        self.coordinates = coordinates[[x],[y]]
        self.orientation = orientation

    # def movement_axis(coordinates[[x],[y]]):
    #     if len(x) > len(y):
    #         # move along the X-axis: left <-> right
    #     elif len(y) > len(x):
    #         # move along the Y-axis: up <-> down
    #     else:
    #         return False "sth wrong with the vehicle"

    def description(self):
        return str(f'vehicle description: {self.name, self.size, self.coordinates, self.orientation}')


    def description(self):
        """
        Returns:
             String containing the name, size and coordinates of the vehicle.
        """
        # TODO: create this function
