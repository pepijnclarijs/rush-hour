import math


class Board:
    """
    This class represents an empty board in a game of rush hour.

    Args:
        length: Integer representing the length of the board.
    """
    def __init__(self, length):
        self.length = length
        
        # Find the box of the finish.
        if length % 2 == 0:
            self.finish = (int(length / 2), length)
        else:
            self.finish = (int(math.ceil(length / 2)), length) 
