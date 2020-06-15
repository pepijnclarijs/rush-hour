import sys
sys.path.append('code/classes')


from game import Game
from board import Board
from vehicle import Vehicle

import csv

def load_game(game_number, board_size):
    vehicles = []
    # Check best result
    with open(f"data/boards/game{game_number}.csv", 'r') as f:
        reader = csv.reader(f)
        next(reader)
        for car, orientation, row, col, length in reader:
            coords = get_coords(orientation, int(row), 7 - int(col), int(length))
            if car == 'X':
                X = Vehicle(car, coords)
                vehicles.append(X)
            else:
                vehicles.append(Vehicle(car, coords))  
            print(car)
            print(coords)
    board = Board(board_size)
    
    game = Game(board, vehicles, X)

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
