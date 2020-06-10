# import sys
# sys.path.append('code/classes')

# from game import Game
# from board import Board
# from vehicle import Vehicle

from code.classes import game, board, vehicle

def load_game(board_size):
    # Create the game board.
    board = board.Board(board_size)

    # Create the begin situation.
    A = vehicle.Vehicle('A', 2, [(1, 2), (1, 3)], 'horizontal')
    B = vehicle.Vehicle('B', 3, [(1, 4), (1, 5), (1, 6)], 'horizontal')
    C = vehicle.Vehicle('C', 2, [(2, 2), (2, 3)], 'horizontal')
    D = vehicle.Vehicle('D', 2, [(2, 4), (3, 4)], 'vertical')
    E = vehicle.Vehicle('E', 2, [(2, 5), (2, 6)], 'horizontal')
    F = vehicle.Vehicle('F', 2, [(3, 3), (4, 3)], 'vertical')
    G = vehicle.Vehicle('G', 2, [(4, 1), (4, 2)], 'horizontal')
    H = vehicle.Vehicle('H', 2, [(4, 4), (4, 5)], 'horizontal')
    I = vehicle.Vehicle('I', 2, [(3, 6), (4, 6)], 'vertical')
    J = vehicle.Vehicle('J', 2, [(5, 1), (6, 1)], 'vertical')
    K = vehicle.Vehicle('K', 2, [(5, 3), (6, 3)], 'vertical')
    L = vehicle.Vehicle('L', 2, [(5, 5), (5, 6)], 'horizontal')

    # Create red car
    X = vehicle.Vehicle('X', 2, [(3, 1), (3, 2)], 'horizontal')

    # Create list of vehicles
    vehicles = [A, B, C, D, E, F, G, H, I, J, K, L, X]

    # Create the game.
    game = game.Game(board, vehicles, X)

    return game

# # load the game
# # Read in the file with the initial GameBoard status.
# def load_initial_board(self, filename):
#     list_vehicles = []
#     vehicle_dict = {}
#     # read cargo file, include information of parcels
#     with open(filename) as csv_data:
#             reader = csv.reader(csv_data, delimiter=',')
#             next(reader)
#             for line in reader:
#                 if "#" in line:
#                     continue
#                 elif line[0].isupper():
#                     vehicle_id = line[0]
#                     size = line[1]
#                     if len(line) is 5:
#                         grid_position = line[2,3]
#                     elif len(line) is 6:
#                         grid_position = line[2,3,4]
#                     else:
#                         # print("incorrect vehicle information")
#                         continue
#                     orientation = line[5]
#                 vehicle_data = Vehicle(name, size, position, orientation)
#                 list_vehicles.append(vehicle_data)
#     return list_vehicles