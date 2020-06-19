import sys

from src.classes.game import Game
from src.classes.board import Board
from src.classes.vehicle import Vehicle
import csv

sys.path.append('src/classes')


def load_game(game_number, board_size):
    vehicles = {}
    # Check best result
    # with open(f"C:\\Users\\pepijn\\PycharmProjects\\rush-hour\\rush-hour\\data\\boards\\game3.csv", 'r') as f:
    with open(f"data/boards/game{game_number}.csv", 'r') as f:
        reader = csv.reader(f)
        next(reader)
        for id, orientation, row, col, length in reader:
            coords = get_coords(orientation, int(row), (board_size + 1) - int(col), int(length))
            vehicles.update({id: Vehicle(id, coords)})

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
