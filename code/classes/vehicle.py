# # class gives particulars about each vehicle object
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


# Suggestie Cecile:

# Class Vehicle:
#     """
#     This class represents a vehicle in a game of rush hour.

#     Args:
#         name: String representing the name for the vehicle.
#         size: Integer representing the length of the vehicle.
#         position: List tuples containing integers. The list represents the position of the vehicle on the board.
#         orientation: String that indicates the direction of the vehicle.
#     """

#     def __init__(self, id, size, position, orientation):
#         self.id = id
#         self.size = size
#         self.position = position
#         self.orientation = orientation

#     def __str__(self):
#         return 'Vehicle object:'str(self.id) + ' of size ' + str(self.size) + ' positioned on gridboxes ' +
#          str(self.position) + ' has a ' + str(self.orientation) + ' orientation.'

#     def move()
