import sys
import csv
from testvehicle import Vehicle

# def load_game(board_size, initial_board):
#     # Create the game board.
#     board_size = 6
#     initial_board = load_initial_board(initial_board)
#
#
# def load_initial_board(initial_board):
initial_board = 'testrush1.csv'

list_vehicles = []
gamestate = {}
# read cargo file, include information of parcels
with open(initial_board) as csv_data:
    reader = csv.reader(csv_data, delimiter=',')
    next(reader)
    for line in reader:
        print(line)
        """ order of csv file vehicle: id, orientation, position first gridbox, size"""
        if line[0].islower():
            continue
        elif line[0].isupper():
            id = line[0]
            print(id)
            orientation = line[1]
            grid_position = line[2:4]
            print(grid_position)
            row = line[2]
            column = line[3]
            size = line[4]
            vehicle_data = Vehicle(id, orientation, row, column, size)
            # gamestate.update({ vehicle_data(id) : [vehicle_data(row)][vehicle_data(column)] })
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

# 2D array
rows, columns = (board_size, board_size)
board_array = [[ 0 for i in range(columns)] for j in range(rows)]
print(f"2D:  {board_array}")

# demonstrate the 2d-array as a board/grid
board_array = [[ 0 for i in range(columns)] for j in range(rows)]
board_array[0][0] = 1
print("2D as a grid :")
for row in board_array:
    print(row)

for (key, value) in gamestate.items():
    board_array[value[0]][value[1]] = key
    print("Gamestate:")
    for row in board_array:
        print(row)



                # print(*list_vehicles)

                # return list_vehicles, gamestate
