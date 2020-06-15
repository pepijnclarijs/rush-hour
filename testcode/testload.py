import sys
import csv

from os import walk
from testvehicle import Vehicle

# def load_game(board_size, initial_board):
#     # Create the game board.
#     board_size = 6
#     initial_board = load_initial_board(initial_board)
#
#
# def load_initial_board(initial_board):

initial_board = sys.argv[1]
#initial_board = 'Rushhour6x6_1.csv'

list_vehicles = []
gamestate = {}
# read cargo file, include information of parcels
with open(initial_board) as csv_data:
    reader = csv.reader(csv_data, delimiter=',')
    next(reader)
    for line in reader:
        # print(line)
        """ order of csv file vehicle: id, orientation, position first gridbox, size"""
        if line[0].islower():
            continue
        elif line[0].isupper():
            id = line[0]
            # print(id)
            orientation = line[1]
            grid_position = line[2:4]
            # print(grid_position)
            row = line[2]
            column = line[3]
            size = line[4]
            vehicle_data = Vehicle(id, orientation, row, column, size)
            # gamestate.update({ vehicle_data(id) : [vehicle_data(row)][vehicle_data(column)] })
            # gamestate.update({ id : (int(row), int(column)) })
            gamestate.update({ id : [int(row), int(column)] })

        else:
            print("something went wrong with the csv_data")

            # print(f"This vehicle has been added: {vehicle_data[0]}")

list_vehicles.append(vehicle_data)


print(f"gamestate dictionary :  \n {gamestate}")
for (key, value) in gamestate.items() :
    print(key , " : ", value )

# 1D array
board_size = 6
row = [0 for i in range(board_size)]
print(f"1D:  {row}")

# # 2D array
rows, columns = (board_size, board_size)
# board_grid = [[ 0 for i in range(columns)] for j in range(rows)]
# print(f"2D:  {board_grid}")

# demonstrate the 2d-array as a board/grid
board_grid = [[ '_' for i in range(columns)] for j in range(rows)]
board_grid[0][0] = 'A'
board_grid[1][5] = 'Z'
print("2D as a grid :")
for row in board_grid:
    print(row)

board_grid = [[ '_' for i in range(columns)] for j in range(rows)]
for key in gamestate.keys(): #reaching the keys of the dict
    hor = int(gamestate[key][0] - 1)
    ver = int(gamestate[key][1] - 1)
    board_grid[hor][ver] = key

    #print(key + " " + str(hor) + " " + str(ver))
    # sth = gamestate.values()

    #print(f"does this work: {hor, ver}???" )
    # print(sth)
    # for value in gamestate[key]: #reaching every element in tuples
    #     print(f"Key {key} has Values {value}")

        # value[0] = row
        # value[1] = column
        # for (row, column) in value:
    # board_grid[row][col] = key
    print("Gamestate:")
    for row in board_grid:
        print(row)
    # print (value[0][1])
    # value.split(',')


    """ equality comparison between gamestates to see if it's unique """

# Rushhour6x6_1.csv [0:8]
initial_board = 'Rushhour12x12_1.csv'
print(initial_board)
print(initial_board[0:8])
print(initial_board[8:])
print(initial_board[8:-4])
list = initial_board[8:-4].split('_')
print(list[0])
print(list[1])
lengte, breedte = list[0].split('x')
print(f"{lengte} is de lengte {breedte} is de breedte")

print(sys.argv)
# print 'Number of arguments:', len(sys.argv), 'arguments.'
#print 'Argument List:', str(sys.argv)

                # print(*list_vehicles)

                # return list_vehicles, gamestate
