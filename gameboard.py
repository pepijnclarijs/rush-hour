import math

# TODO: I called stuff x and y but is should all be changed to row and column. Otherwise it would lead to a lot of /
# 	confusion since a coordinate system names the horizontal axis the x axis and the vertical axis the y axis. /
# 	Now I use the x axis to indicate the rows which would be logically/visually the y axis in a normal coordinate /
# 	system.

# TODO: Maybe change the variable name 'exit' because it shadows a built-in function.

# TODO: The code in the get_passed_coor function is now dependent of how the coordinates of a vehicle are implemented.
# 	It should now be implemented in this way: if horizontal: [(left most coor), (middle coor), (right most coor)].
# 	If vertical: [(lower coor), (middle coor), (upper coor)]


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

        # Get the box that is in front of the exit.
        exit = self.get_board().get_exit()

        # Get the boxes between the exit and the red car.
        box = self.red_car.get_position()[1]
        while box != exit:
            # Get the next spot
            next_row = box[0]
            next_column = box[1] + 1
            next_spot = (next_row, next_column)

            # Loop over all vehicles on the board.
            for vehicle in self.get_vehicles():
                # Check if a vehicle is blocking the exit.
                if next_spot in vehicle.get_position():
                    # If a vehicle is blocking the exit, the game is not finished.
                    return False

            box = (next_row, next_column)

            # Check if the exit is reached.
            if box == exit:
                # If all spots between the red car and the exit are free, the game is finished.
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


class Board:
    """
    This class represents an empty board in a game of rush hour.

    Args:
        length: Integer representing the length of the board.
    """

    def __init__(self, length):
        self.length = length

        # TODO: Maybe make exit a pair of coordinates (indicating the red car is at that position would be easier that way)

        # Find the box of the exit.
        if length % 2 == 0:
            self.exit = (int(length / 2), length)
        else:
            self.exit = (int(math.ceil(length / 2)), length)

    # TODO: Would it be better to define an upper, lower, right and left border instead of just using the length /
    #  whenever it is needed to indicate the borders of the board? That would get rid of some magic numbers /
    #  (the 1 in x_coor < 1 and y_coor < 1) in the is_move allowed function above. However it would cost many /
    #  lines of code (because of including getters for / these attributes).

    def get_length(self):
        """
        Returns:
            Integer indicating the length of the board.
        """

        return self.length

    def get_exit(self):
        """
        Returns:
            Tuple of integers indicating the box that is in front of the exit.
        """
        return self.exit


class Vehicle:
    """
    This class represents a vehicle in a game of rush hour.

    Args:
        name: String representing the name for the vehicle.
        size: Integer representing the length of the vehicle.
        position: List tuples containing integers. The list represents the position of the vehicle on the board.
        orientation: String that indicates the direction of the vehicle.
    """

    def __init__(self, name, size, position, orientation):
        self.name = name
        self.size = size
        self.position = position
        self.orientation = orientation

    def get_name(self):
        """
        Returns:
            String indicating the name of the vehicle.
        """

        return self.name

    def get_size(self):
        """
        Returns:
            Integer indicating the size of the vehicle.
        """

        return self.size

    def get_position(self):
        """
        Returns:
            List tuples containing integers. The list represents the position of the vehicle on the board.
        """

        return self.position

    def set_position(self, new_position):
        """
        Changes the position of the vehicle.

        Args:
            new_position: List of tuples that hold a position. It indicates the future location of the vehicle.
        """
        self.position = new_position

    def get_orientation(self):
        """
        Returns:
            String indicating the orientation of the vehicle.
        """

        return self.orientation

    def description(self):
        """
        Returns:
            String containing the name, size and position of the vehicle.
        """
        return f"Vehicle {self.get_name()} of size {self.get_size} at position {self.get_position()} with " \
               f"orientation {self.get_orientation()}"

    def speculate_new_position(self, steps):
        """
        Speculates the new position of the vehicle after moving by a number of steps.

        Args:
            steps: Integer representing the number of steps the vehicle would move.

        Returns:
            List of tuples indicating the would be new position of the vehicle after moving by a number of steps.
        """

        # Get the position and orientation of the vehicle.
        orientation = self.get_orientation()
        position = self.get_position()

        # Loop over the position.
        new_position = []
        for box in position:
            # Get the row and column.
            row = box[0]
            column = box[1]

            # Check which one should be changed.
            if orientation == 'horizontal':
                new_column = box[1] + steps
                # Create the new position of the vehicle.
                new_position.append((row, new_column))
            else:
                new_row = box[0] + steps
                # Create the new position of the vehicle.
                new_position.append((new_row, column))

        return new_position

    def get_passed_boxes(self, end_position):
        """
        Gets the boxes that are passed when a vehicle moves from its place to the 'end_box' box.

        Args:
            end_position: Tuple representing the position up until which the passed boxes should be found.

        Returns:
            List of tuples that represent the boxes between the vehicle and the given end position.
        """

        # TODO: use the name 'start_position' instead of 'vehicle_position'.

        # Get the position, orientation and size of the vehicle.
        orientation = self.get_orientation()
        vehicle_position = self.get_position()

        # TODO: make the below a little cleaner.
        # Make place for the enclosed boxes.
        enclosed_boxes = []

        # Check the orientation of the vehicle.
        if orientation == 'horizontal':
            # Sort the boxes representing the vehicle position on column value.
            sorted_boxes = sorted(vehicle_position, key=lambda pair: pair[1])

            # Get the right most box.
            vehicle_right_most_box = sorted_boxes[-1]

            # Get the left most box.
            vehicle_left_most_box = sorted_boxes[0]

            # Sort the boxes in the end position based on column values from small to large.
            sorted_end_position = sorted(end_position, key=lambda pair: pair[1])

            # Get the left most and right most box of the end position.
            end_position_left_most_box = sorted_end_position[0]
            end_position_right_most_box = sorted_end_position[-1]

            # Check if the end position is to the right of the vehicle.
            if end_position_left_most_box[1] >= vehicle_right_most_box[1]:
                # Get the number of boxes between the vehicle and its end position.
                enclosed_boxes_count = end_position_left_most_box[1] - vehicle_right_most_box[1]

                # Get the enclosed boxes. # TODO: put this in a helper function.
                for i in range(1, enclosed_boxes_count):
                    enclosed_box = (vehicle_right_most_box[0], vehicle_right_most_box[1] + i)
                    enclosed_boxes.append(enclosed_box)
            else:
                # Get the number of boxes between the vehicle and its end position.
                enclosed_boxes_count = vehicle_left_most_box[1] - end_position_right_most_box[1]

                # Get the enclosed boxes. # TODO: put this in a helper function.
                for i in range(1, enclosed_boxes_count):
                    enclosed_box = (vehicle_left_most_box[0], vehicle_left_most_box[1] - i)
                    enclosed_boxes.append(enclosed_box)
        else:
            # Sort the boxes representing the vehicle position on row value.
            sorted_boxes = sorted(vehicle_position, key=lambda pair: pair[0])

            # Get the lower most box of the vehicle.
            vehicle_lower_most_box = sorted_boxes[-1]

            # Get the upper most box of the vehicle.
            vehicle_upper_most_box = sorted_boxes[0]

            # Sort the boxes in the end position based on row values from small to large.
            sorted_end_position = sorted(end_position, key=lambda pair: pair[0])

            # Get the upper and lower most box of the end position.
            end_position_upper_most_box = sorted_end_position[0]
            end_position_lower_most_box = sorted_end_position[-1]

            # Check if the end position is above the vehicle.
            if end_position_lower_most_box[0] <= vehicle_upper_most_box[0]:
                enclosed_boxes_count = vehicle_upper_most_box[0] - end_position_lower_most_box[0]

                # Get the enclosed boxes. # TODO: put this in a helper function.
                for i in range(1, enclosed_boxes_count):
                    enclosed_box = (vehicle_upper_most_box[0] - i, vehicle_upper_most_box[1])
                    enclosed_boxes.append(enclosed_box)
            else:
                enclosed_boxes_count = end_position_upper_most_box[0] - vehicle_lower_most_box[0]

                # Get the enclosed boxes. # TODO: put this in a helper function.
                for i in range(1, enclosed_boxes_count):
                    enclosed_box = (vehicle_lower_most_box[0] + i, vehicle_lower_most_box[1])
                    enclosed_boxes.append(enclosed_box)

        return enclosed_boxes

    def move(self, new_position):
        """
        Moves a vehicle by a number of 'steps'.

        Args:
            new_position: List of tuples indicating the position of the vehicle.

        Returns:
            None
        """

        # TODO: This function is not necessary I think. set_position does exactly the same right?

        self.set_position(new_position)
