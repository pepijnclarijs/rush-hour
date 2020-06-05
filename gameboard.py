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

    def move(vehicle, steps):
        """
        Moves a vehicle by an amount of 'steps'.

        Args:
            vehicle: Vehicle that is moved.
            steps: Integer representing the number of steps the vehicle should move.

        Returns:
             Boolean indicating whether the vehicle was successfully moved or not.
        """

        # Get the coordinates and orientation of the vehicle.
        orientation = vehicle.get_orientation()
        coordinate_pairs = vehicle.get_coordinates()

        # Loop over the coordinate pairs.
        new_coordinates = []
        for coordinates in coordinate_pairs:
            # Get the x and y coordinates.
            x_coordinate = coordinates[0]
            y_coordinate = coordinates[1]

            # Check which coordinate should change.
            if orientation == 'x':
                new_x_coordinate = coordinates[0] + steps
                # Create the new coordinates of the vehicle.
                new_coordinates.append([new_x_coordinate, y_coordinate])
            else:
                new_y_coordinate = coordinates[1] + steps
                # Create the new coordinates of the vehicle.
                new_coordinates.append([x_coordinate, new_y_coordinate])

        # Check if the new coordinates are valid.
        # Pseudo code:
        # if gameboard.is_move_allowed(coordinates):
        #   # Set the new coordinates of the vehicle.
        #   vehicle.set_coordinates(new_coordinates)
        #   return True
        # else:
        #   return False
        # TODO: write this function

        def is_move_allowed(self, coordinate_pairs):
            """
            Checks if a move is allowed by checking whether the coordinates are not occupied and lie within the field of the
            game.

            Args:
                coordinate_pairs: list of pairs of coordinates indicating the position of the vehicle.

            Returns:
                 Boolean indicating whether the vehicle is allowed to move to the given position.
            """
            # Get all coordinates that are not allowed.
            # Pseudo code:
            # # Loop over all vehicles on the board.
            # for vehicle in self.vehicles:
            #     # Loop over all coordinates that need to be checked.
            #     for coordinates in coordinate_pairs:
            #         # Check if the coordinate is free.
            #         if coordinates == vehicle.get_coordinates():
            #             return False
            #         # Check if x and y coordinate are inside the board.
            #         x_coor = coordinates[0]
            #         y_coor = coordinates[1]
            #         if (x_coor < left_border or x_coor > right_border or y_coor < lower_border or y_coor > upper_border):
            #             return False
            # return True
            pass

class Board:
    """
    This class represents an empty board in a game of rush hour.
w
    Args:
        length: Integer representing the length of the board.
    """
    def __init__(self, length):
        # TODO: create a grid that contains a value that represents an empty spot.
        pass


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





