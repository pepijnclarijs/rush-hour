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
            self.taken_boxes.extend(vehicle.get_position())

    def get_board(self):
        return self.board

    def get_vehicles(self):
        return self.vehicles

    def get_taken_boxes(self):
        return self.taken_boxes

    def update_taken_boxes(self):
        taken_positions = []
        for vehicle in self.vehicles:
            taken_positions.extend(vehicle.get_position())
        self.taken_boxes = taken_positions

    def description(self):
        return f"{self.board} contains: {self.vehicles}."

    def is_finished(self):
        """
		Returns:
			Boolean Indicating whether the game is won or not.
		"""

        # Get the box that is in front of the finish.
        finish = self.get_board().get_finish()

        # Get the boxes between the finish and the red car.
        box = self.red_car.get_position()[1]
        while box != finish:
            # Get the next spot
            next_row = box[0]
            next_column = box[1] + 1
            next_spot = (next_row, next_column)

            # Loop over all vehicles on the board.
            for vehicle in self.get_vehicles():
                # Check if a vehicle is blocking the finish.
                if next_spot in vehicle.get_position():
                    # If a vehicle is blocking the finish, the game is not finished.
                    return False

            box = (next_row, next_column)

            # Check if the finish is reached.
            if box == finish:
                # If all spots between the red car and the finish are free, the game is finished.
                return True

    def is_move_allowed(self, moving_vehicle, end_position):
        """
        Checks if a move is allowed by checking whether the passed boxes are not occupied and lie within the board.

        Args:
            end_position: List of tuples indicating the end position of the vehicle.
            moving_vehicle: The vehicle that is moving to the end position indicated by end_position argument.

        Returns:
            Boolean indicating whether the vehicle is allowed to move to the given position.
        """

        # Get all boxes that are passed when the vehicle moves to its end position.
        passed_boxes = moving_vehicle.get_passed_boxes(end_position)

        # Add the end position itself as well.
        passed_boxes.extend(end_position)

        # Get all taken boxes.
        taken_boxes = self.get_taken_boxes()
        for box in passed_boxes:
            # Skip the boxes that are already taken by the current vehicle.
            if box in moving_vehicle.get_position():
                continue
            # Check if the box is taken.
            if box in taken_boxes:
                return False

            # TODO: this could be optimized a little by only checking for the outer most box taken by the vehicle to be
            #  on the board.
            # Check if the row and column are inside the board.
            row = box[0]
            column = box[1]
            board = self.get_board()
            if (row < 1
                    or row > board.get_length()
                    or column < 1
                    or column > board.get_length()):
                return False
        return True
        