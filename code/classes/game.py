class Game:
    """
    This class represents a game of rush hour.

    Args:
        board: This is an instance of an empty game board.
        vehicles: This is a list containing the vehicles present in the game.
    """
    def __init__(self, board, vehicles, red_car):
        self.board = board
        self.vehicles = vehicles
        self.red_car = red_car

        # Remember the taken boxes on the board.
        self.taken_boxes = []
        for vehicle in self.vehicles:
            self.taken_boxes.extend(vehicle.position)

    def update_taken_boxes(self):
        """
        Updates the list that keeps track of the boxes that are taken.
        """
        taken_positions = []
        for vehicle in self.vehicles:
            taken_positions.extend(vehicle.position)
        self.taken_boxes = taken_positions

    def is_finished(self):
        """
        Returns:
            Boolean Indicating whether the game is won or not.
        """
        if self.board.finish == self.red_car.position[1]:
            return True

        return False

    def validate_move(self, vehicle, end_position):
        """
        Checks if a move is allowed by checking whether the passed boxes are not occupied and lie within the board.

        Args:
            end_position: List of tuples indicating the end position of the vehicle.
            vehicle: The vehicle that is moving to the end position indicated by end_position argument.

        Returns:
            Boolean indicating whether the vehicle is allowed to move to the given position.
        """
        # Get all boxes that are passed when the vehicle moves to its end position.
        passed_boxes = vehicle.get_passed_boxes(end_position)

        # Add the end position itself as well.
        passed_boxes.extend(end_position)

        # Get all taken boxes
        for box in passed_boxes:
            # Skip the boxes that are already taken by the current vehicle.
            if box in vehicle.position:
                continue
            # Check if the box is taken.
            if box in self.taken_boxes:
                return False

            # Check if the row and column are inside the board.
            row = box[0]
            column = box[1]
            board = self.board
            if (row < 1
                    or row > board.length
                    or column < 1
                    or column > board.length):
                return False

        return True

    def move(self, vehicle, end_position):
        """
        Moves a vehicle in the game from its current position to end_position.

        Args:
            vehicle: The vehicle that is moved.
            end_position: List of tuples containing integers representing a row and a column [(i, j), (i, j)]. The position
                            to which the vehicle is moved.
        """

        # Move the vehicle.
        vehicle.set_position(end_position)

        # Update the list that contains the taken boxes.
        self.update_taken_boxes()
