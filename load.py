import sys
sys.path.append('code/classes')

# from game import Game
# from board import Board
# from vehicle import Vehicle

from code.classes import game, board, vehicle
import csv
# from main import game_number

def load_game(board_size, initial_board):
    # Create the game board.
    board_size = board.Board(board_size)
    initial_board = load_initial_board(initial_board)

def load_initial_board(initial_board):
    list_vehicles = []
    gamestate = {}
    # read cargo file, include information of parcels
    with open(initial_board) as csv_data:
            reader = csv.reader(csv_data, delimiter=',')
            next(reader)
            for line in reader:
                """ order of csv file vehicle: id, position gridboxes, orientation, size"""
                if "#" in line:
                    continue
                elif line[0].isupper():
                    id = line[0]
                    if len(line) is 5: # if line.range(5):
                        grid_position = line[1:3]
                        orientation = line[3]
                        size = line[4]
                    elif len(line) is 6:
                        grid_position = line[1:4]
                        orientation = line[4]
                        size = line[5]
                    else:
                        print("incorrect vehicle information")

                    vehicle_data = vehicle.Vehicle(id, size, grid_position, orientation)
                    # print(f"This vehicle has been added: {vehicle_data[0]}")
                    gamestate.update({ id : grid_position })

                    list_vehicles.append(vehicle_data)

            print(f"gamestate dictionary :  \n {gamestate}")
            for (key, value) in gamestate.items() :
                print(key , " : ", value )

                        # print(*list_vehicles)

    return list_vehicles, gamestate
    # Create the begin situation.
    # A = vehicle.Vehicle('A', 2, [(1, 2), (1, 3)], 'horizontal')
    # B = vehicle.Vehicle('B', 3, [(1, 4), (1, 5), (1, 6)], 'horizontal')
    # C = vehicle.Vehicle('C', 2, [(2, 2), (2, 3)], 'horizontal')
    # D = vehicle.Vehicle('D', 2, [(2, 4), (3, 4)], 'vertical')
    # E = vehicle.Vehicle('E', 2, [(2, 5), (2, 6)], 'horizontal')
    # F = vehicle.Vehicle('F', 2, [(3, 3), (4, 3)], 'vertical')
    # G = vehicle.Vehicle('G', 2, [(4, 1), (4, 2)], 'horizontal')
    # H = vehicle.Vehicle('H', 2, [(4, 4), (4, 5)], 'horizontal')
    # I = vehicle.Vehicle('I', 2, [(3, 6), (4, 6)], 'vertical')
    # J = vehicle.Vehicle('J', 2, [(5, 1), (6, 1)], 'vertical')
    # K = vehicle.Vehicle('K', 2, [(5, 3), (6, 3)], 'vertical')
    # L = vehicle.Vehicle('L', 2, [(5, 5), (5, 6)], 'horizontal')

    # # Create red car
    # X = vehicle.Vehicle('X', 2, [(3, 1), (3, 2)], 'horizontal')
    #
    # # Create list of vehicles
    # vehicles = [A, B, C, D, E, F, G, H, I, J, K, L, X]

    # Create the game.
    game = Game(board_size, list_vehicles, X)

    return game

# # load the game
# # Read in the file with the initial GameBoard status.
#in init
