import sys
sys.path.append('code/classes')

from game import Game
from board import Board
from vehicle import Vehicle

from code.classes import game, board, vehicle

def load_game(board_size):
    # Create the game board.
    board = Board(board_size)

    # Create the begin situation.
    A = Vehicle('A', [(1, 2), (1, 3)])
    B = Vehicle('B', [(1, 4), (1, 5), (1, 6)])
    C = Vehicle('C', [(2, 2), (2, 3)])
    D = Vehicle('D', [(2, 4), (3, 4)])
    E = Vehicle('E', [(2, 5), (2, 6)])
    F = Vehicle('F', [(3, 3), (4, 3)])
    G = Vehicle('G', [(4, 1), (4, 2)])
    H = Vehicle('H', [(4, 4), (4, 5)])
    I = Vehicle('I', [(3, 6), (4, 6)])
    J = Vehicle('J', [(5, 1), (6, 1)])
    K = Vehicle('K', [(5, 3), (6, 3)])
    L = Vehicle('L', [(5, 5), (5, 6)])

    # Create red car
    X = Vehicle('X', [(3, 1), (3, 2)])

    # Create list of vehicles
    vehicles = [A, B, C, D, E, F, G, H, I, J, K, L, X]

    # Create the game.
    game = Game(board, vehicles, X)

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