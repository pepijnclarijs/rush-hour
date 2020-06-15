import sys
sys.path.append('src/classes')

from src.classes.game import Game
from src.classes.board import Board
from src.classes.vehicle import Vehicle

import csv

def load_game(game_number, board_size):
    vehicles = []
    # Check best result
    with open("C:\\Users\\pepijn\\PycharmProjects\\rush-hour\\rush-hour\\data\\boards\\game1.csv", 'r') as f:
        reader = csv.reader(f)
        next(reader)
        for car, orientation, row, col, length in reader:
            coords = get_coords(orientation, int(row), (board_size + 1) - int(col), int(length))
            if car == 'X':
                X = Vehicle(car, coords)
                vehicles.append(X)
            else:
                vehicles.append(Vehicle(car, coords))
    board = Board(board_size)

    game = Game(board, vehicles)

    return game

def get_coords(orientation, row, col, length):
    # Check which one should be changed.
    coords = []
    for i in range(length):
        if orientation == 'H':
            coords.append((col, row + i))
        elif orientation == 'V':
            coords.append((col - i, row))
        else:
            print("Error loading CSV")
            break
    return coords

# # from main import game_number
# def load_game(board_size):
#     # Create the game board.
#     board_size = board.Board(board_size)
#     initial_board = load_initial_board(initial_board)


# def load_initial_board(initial_board):
#     list_vehicles = []
#     gamestate = {}
#     # read cargo file, include information of parcels
#     with open(initial_board) as csv_data:
#             reader = csv.reader(csv_data, delimiter=',')
#             next(reader)
#             for line in reader:
#                 """ order of csv file vehicle: id, orientation, position first gridbox, size"""
#                 if line[0].islower():
#                     continue
#                 elif line[0].isupper():
#                     id = line[0]
#                     orientation = line[1]
#                     grid_position = line[2:4]
#                     row = line[2]
#                     column = line[3]
#                     size = line[4]
#                 else:
#                     print("something went wrong with the csv_data")

#                     vehicle_data = vehicle.Vehicle(id, orientation, row, column, size)
#                     # print(f"This vehicle has been added: {vehicle_data[0]}")
#                     gamestate.update({ id : [row][column] })

#                     list_vehicles.append(vehicle_data)

#             print(f"gamestate dictionary :  \n {gamestate}")
#             for (key, value) in gamestate.items() :
#                 print(key , " : ", value )


#                         # print(*list_vehicles)

#     return list_vehicles, gamestate
#     # # Create the begin situation.
#     # A = Vehicle('A', [(1, 2), (1, 3)])
#     # B = Vehicle('B', [(1, 4), (1, 5), (1, 6)])
#     # C = Vehicle('C', [(2, 2), (2, 3)])
#     # D = Vehicle('D', [(2, 4), (3, 4)])
#     # E = Vehicle('E', [(2, 5), (2, 6)])
#     # F = Vehicle('F', [(3, 3), (4, 3)])
#     # G = Vehicle('G', [(4, 1), (4, 2)])
#     # H = Vehicle('H', [(4, 4), (4, 5)])
#     # I = Vehicle('I', [(3, 6), (4, 6)])
#     # J = Vehicle('J', [(5, 1), (6, 1)])
#     # K = Vehicle('K', [(5, 3), (6, 3)])
#     # L = Vehicle('L', [(5, 5), (5, 6)])

#     # # Create red car
#     # X = Vehicle('X', [(3, 1), (3, 2)])

#     # # Create list of vehicles
#     # vehicles = [A, B, C, D, E, F, G, H, I, J, K, L, X]

#     # for vehicle in list_vehicles:
#     #     if vehicle.id == 'X'
#     #         vehicle = red_car
#     #     return red_car
#     # Create the game.
#     game = Game(board_size, list_vehicles, red_car)

#     # return game

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
