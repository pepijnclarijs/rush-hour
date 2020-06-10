import math

class Board:
    """
    This class represents an empty board in a game of rush hour.

    Args:
        length: Integer representing the length of the board.
    """

    def __init__(self, length):
        self.length = length

        # TODO: Maybe make finish a pair of coordinates (indicating the red car is at that position would be easier that way)

        # Find the box of the finish.
        if length % 2 == 0:
            self.finish = (int(length / 2), length)
        else:
            self.finish = (int(math.ceil(length / 2)), length)

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

    def get_finish(self):
        """
        Returns:
            Tuple of integers indicating the box that is in front of the finish.
        """
        return self.finish



