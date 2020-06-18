# Game class representing a game of rush hour.

from src.util import get_red_car

# TODO: Get rid of unneccessary attributes.
class Game:
    """
    This class represents a game of rush hour.

    Args:
        board (Board): This is an instance of an empty game board.
        vehicles (dict of str: Vehicle): This is a list containing the vehicles present in the game.

    Attributes:
        board (Board): Represents a board for a game of rush hour.
        vehicles (dict of str: Vehicle): Represents vehicles that can be placed on the board.
        red_car (Vehicle): Represents the red car.
        current_state (dict of str: list of tuples of integers): Represents the current state that the game is in.
        states (list of dict of str: list of tuples of integers): Represents the states that the game has been in.
        possible_moves (set of tuples of Vehicle, integer): Represents the possible moves that can be done in the
                current state of the game.
    """
# TODO: Make sure everything is updated correctly. The red car for example is not at the moment.
    def __init__(self, board, vehicles):
        self.board = board
        self.vehicles = vehicles
        self.red_car = get_red_car(self)
        self.current_state = {}
        self.states = []
        self.possible_moves = set()
        self.taken_boxes = []
        self.executed_moves = []

        # Initialize attributes.
        self.update_current_state()
        self.update_states()
        self.update_taken_boxes()
        self.update_possible_moves()

    def update_vehicles(self, update_vehicle):
        """
        Updates vehicle object in the list of vehicles.

        Args:
            update_vehicle (Vehicle): The vehicle in the vehicle list that should be updated.
        """

        updated_vehicles = {}
        for vehicle in self.vehicles.values():
            if vehicle.id == update_vehicle.id:
                vehicle = update_vehicle
            updated_vehicles[vehicle.id] = vehicle
        self.vehicles = updated_vehicles

    def update_current_state(self):
        """
        Updates the current_state dictionary.
        """

        self.current_state = {}
        for vehicle in self.vehicles.values():
            self.current_state.update({vehicle.id: vehicle.position})

    def update_states(self):
        """
        Updates the dictionary that holds the states.

        NOTE: The dict should not be emptied before updates as in the other update functions. We want to remember all
        states.
        """

        self.states.append(self.current_state)

    def update_taken_boxes(self):
        """
        Updates the list that keeps track of the boxes that are taken.
        """
        taken_positions = []
        for vehicle in self.vehicles.values():
            taken_positions.extend(vehicle.position)
        self.taken_boxes = taken_positions

    def update_possible_moves(self):
        """
        Updates the possible_moves set.
        """

        self.possible_moves = set()
        for vehicle in self.vehicles.values():
            # Get the possible moves in the current state.
            for steps in range(-self.board.length + vehicle.size, self.board.length - vehicle.size):
                if steps == 0:
                    continue
                new_coordinates = vehicle.speculate_new_position(steps)
                if self.validate_move(vehicle, new_coordinates):
                    move = (vehicle, steps)
                    self.possible_moves.add(move)

    def update_executed_moves(self, move):
        self.executed_moves.append(move)

    def is_finished(self):
        """
        Returns:
            Boolean Indicating whether the game is won or not.
        """
        if self.board.finish_position == self.red_car.position:
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

        passed_boxes = vehicle.get_passed_boxes(end_position)

        # Loop over the passed boxes.
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

        # Update red car if necessary.
        if vehicle.id == 'X':
            self.red_car = vehicle

        # Update attributes.
        self.update_vehicles(vehicle)
        self.update_taken_boxes()
        self.update_current_state()
        self.update_states()
        self.update_possible_moves()
