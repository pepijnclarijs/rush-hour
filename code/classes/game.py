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

    def validate_move(self, vehicle, end_position):
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
