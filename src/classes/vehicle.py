from src.util import get_enclosed_boxes


class Vehicle:
    """
    This class represents a vehicle in a game of rush hour.

    Args:
        id (str): The id of the vehicle.
        position (List tuples containing integers [(i_1, j_1),(i_2, j_2)]) : The position of the vehicle on
                the board.

    Attributes:
        id (str): The id of the vehicle.
        position (List tuples containing integers [(i_1, j_1),(i_2, j_2)]): The position of the vehicle.
        color (str): Represents the color of the vehicle.
        orientation (str): The orientation of the vehicle.
        size (int): The size of the vehicle (number of boxes on the grid that it occupies).

    """
    def __init__(self, id, position):
        self.id = id
        self.position = position
        self.color = None

        # Check if both boxes are in the same row.
        if self.position[0][0] == self.position[1][0]:
            self.orientation = 'horizontal'

            # Sort the boxes in the position based on column values from small to large.
            sorted_position = sorted(position, key=lambda pair: pair[1])

            # Calculate the size of the vehicle.
            self.size = 1 + sorted_position[1][1] - sorted_position[0][1]
        else:
            self.orientation = 'vertical'

            # Sort the boxes representing the vehicle position on row value from small to large.
            sorted_position = sorted(position, key=lambda pair: pair[0])

            # Calculate the size of the vehicle.
            self.size = 1 + sorted_position[1][0] - sorted_position[0][0]

    def get_position(self):
        return self.position

    def set_position(self, new_position):
        self.position = new_position

    def speculate_new_position(self, steps):
        """
        Speculates the new position of the vehicle after moving by a number of steps.

        Args:
            steps (int): The number of steps the vehicle would move.

        Returns:
            List of tuples containing integers [(i_1, j_1),(i_2, j_2)] indicating the would be new position of the
            vehicle after moving by a number of steps.
        """
        # Loop over the position.
        new_position = []
        for box in self.position:
            # Get the row and column.
            row, column = box

            # Check which one should be changed.
            if self.orientation == 'horizontal':
                new_column = column + steps
                # Create the new position of the vehicle.
                new_position.append((row, new_column))
            else:
                new_row = row + steps
                # Create the new position of the vehicle.
                new_position.append((new_row, column))

        return new_position

    def get_passed_boxes(self, end_position):
        """
        Gets the boxes that are passed when a vehicle moves from its place to the 'end_box' box.

        Args:
            end_position (Tuple of integers (i, j)): Represents the position up until which the passed boxes should be
            found.
        Returns:
            List of tuples containing integers [(i_1, j_1),(i_2, j_2)] that represent the boxes between the vehicle and
            the given end position.
        """

        passed_boxes = []
        # Add the end position to passed boxes list.
        for box in end_position:
            passed_boxes.append(box)

        # Get the enclosed boxes between the vehicle and its end position.
        enclosed_boxes = get_enclosed_boxes(self.position[0], end_position[0])

        # Add the enclosed boxes to the passed boxes.
        for box in enclosed_boxes:
            # Check if the box is not already in the list.
            if box not in passed_boxes:
                passed_boxes.append(box)

        return passed_boxes

    def equals(self, other):
        if self.id == other.id and self.position == other.position:
            return True
        else:
            return False

    def __repr__(self):
        return f"Vehicle {self.id}: ({self.position})"
