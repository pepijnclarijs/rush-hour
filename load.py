import csv, sys

from src.classes.game import Game
from src.classes.board import Board
from src.classes.vehicle import Vehicle


def load_game(game_number, board_size):
    vehicles = {}

    # with open(f"C:\\Users\\pepijn\\PycharmProjects\\rush-hour\\rush-hour\\data\\boards\\game3.csv", 'r') as f:
    with open(f"data/boards/game{game_number}.csv", 'r') as f:
        reader = csv.reader(f)
        next(reader)
        for id, orientation, row, col, length in reader:
            coords = get_coords(orientation, int(row), (board_size + 1) - int(col), int(length))
            vehicles[id] = Vehicle(id, coords)

    board = Board(board_size)
    game = Game(board, vehicles)

    return game


def get_coordinates(orientation, row, col, length):
    # Generate coordinates 
    coordinates = []
    for i in range(length):
        if orientation == 'H':
            coordinates.append((col, row + i))
        elif orientation == 'V':
            coordinates.append((col - i, row))
        else:
            sys.exit('Error loading CSV file')
    return coordinates
