from gameboard import Game, Board, Vehicle
import random

# TODO: 1) Create a list of vehicles with the horizontal coordinates.
#   2) Make an instance of the game class.
#   3) Write the finished function in the game class
#   4) Move vehicles around and save the movement in the excel format (car, move)
#   5) When the win condition is met, stop moving and print the list of moves.

# Solve the game 10 times.
solved_cases = {}
for i in range(10):
    # Create the 6x6 game board.
    board = Board(6)

    # Create the begin situation.
    A = Vehicle('A', 2, [(1, 2), (1, 3)], 'horizontal')
    B = Vehicle('B', 3, [(1, 4), (1, 5), (1, 6)], 'horizontal')
    C = Vehicle('C', 2, [(2, 2), (2, 3)], 'horizontal')
    D = Vehicle('D', 2, [(2, 4), (3, 4)], 'vertical')
    E = Vehicle('E', 2, [(2, 5), (2, 6)], 'horizontal')
    X = Vehicle('X', 2, [(3, 1), (3, 2)], 'horizontal')
    F = Vehicle('F', 2, [(3, 3), (4, 3)], 'vertical')
    G = Vehicle('G', 2, [(4, 1), (4, 2)], 'horizontal')
    H = Vehicle('H', 2, [(4, 4), (4, 5)], 'horizontal')
    I = Vehicle('I', 2, [(3, 6), (4, 6)], 'vertical')
    J = Vehicle('J', 2, [(5, 1), (6, 1)], 'vertical')
    K = Vehicle('K', 2, [(5, 3), (6, 3)], 'vertical')
    L = Vehicle('L', 2, [(5, 5), (5, 6)], 'horizontal')

    vehicles = [A, B, C, D, E, F, G, H, I, J, K, L, X]

    # Create the game.
    game = Game(board, vehicles)

    # Create a list to track the movements.
    moves = []

    # Read in the file with the initial GameBoard status.
    def load_initial_board(self, filename):
        list_vehicles = []
        vehicle_dict = {}
        # read cargo file, include information of parcels
        with open(filename) as csv_data:
                reader = csv.reader(csv_data, delimiter=',')
                next(reader)
                for line in reader:
                    if "#" in line:
                        continue
                    elif line[0].isupper():
                        vehicle_id = line[0]
                        size = line[1]
                        if len(line) is 5:
                            grid_position = line[2,3]
                        elif len(line) is 6:
                            grid_position = line[2,3,4]
                        else:
                            # print("incorrect vehicle information")
                            continue
                        orientation = line[5]
                    vehicle_data = Vehicle(name, size, position, orientation)
                    list_vehicles.append(vehicle_data)
        return list_vehicles
    # Move vehicles around randomly until the game is finished.
    j = 0
    while not game.is_finished():
        # Get a random number of steps.
        steps = 0
        while steps == 0:
            steps = random.randint(-4, 4)

        # Get a random vehicle.
        random_vehicle = vehicles[random.randint(0, 12)] # Magic number random nummer tussen 0 en 12

        # Speculate the new position passed by the vehicle.
        new_coordinates = random_vehicle.speculate_new_position(steps)

        # Check if the new position is free.
        test = game.is_move_allowed(random_vehicle, new_coordinates)
        if test:
            # Move the vehicle to the new position.
            random_vehicle.move(new_coordinates)
            game.update_taken_boxes()
        else:
            continue

        # Save the movements of the vehicles.
        move = (random_vehicle.get_name(), steps)
        moves.append(move)

        j += 1
        if j > 1000:
            moves = "oops! Something went wrong."
            break

        solved_cases[f"{i}"] = moves

first_iter = True
previous_case = None
for case in solved_cases:
    if first_iter:
        previous_case = case
        first_iter = False
    if len(solved_cases[case]) < len(solved_cases[previous_case]):
        previous_case = case
print(f"The case with the least number of moves is case {previous_case} with {len(solved_cases[previous_case])} moves.")
print(f"The moves are: {solved_cases[previous_case]}")
