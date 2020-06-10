class Vehicle:
    """
    This class represents a vehicle in a game of rush hour.

    Args:
        id: String representing the name for the vehicle.
        size: Integer representing the length of the vehicle.
        position: List tuples containing integers. The list represents the position of the vehicle on the board.
        orientation: String that indicates the direction of the vehicle.
    """
    def __init__(self, id, size, position, orientation):
        self.id = id
        self.size = size
        self.position = position
        self.orientation = orientation

    def get_position(self):
        return self.position

    def set_position(self, new_position):
        self.position = new_position

    def speculate_new_position(self, steps):
        """
        Speculates the new position of the vehicle after moving by a number of steps.

        Args:
            steps: Integer representing the number of steps the vehicle would move.

        Returns:
            List of tuples indicating the would be new position of the vehicle after moving by a number of steps.
        """
        # Loop over the position.
        new_position = []
        for box in self.position:
            # Get the row and column.
            row = box[0]
            column = box[1]

            # Check which one should be changed.
            if self.orientation == 'horizontal':
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
        enclosed_boxes = []

        # Check the orientation of the vehicle.
        if self.orientation == 'horizontal':
            # Sort the boxes representing the vehicle position on column value.
            sorted_boxes = sorted(self.position, key=lambda pair: pair[1])

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
            sorted_boxes = sorted(self.position, key=lambda pair: pair[0])

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