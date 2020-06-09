from gameboard import Game, Board, Vehicle
import random
import csv
import time

# TODO: 1) Create a list of vehicles with the horizontal coordinates.
#   2) Make an instance of the game class.
#   3) Write the finished function in the game class
#   4) Move vehicles around and save the movement in the excel format (car, move)
#   5) When the win condition is met, stop moving and print the list of moves.

# set amount of runs
runs = 10
board_size = 6

start_time = time.time()

# Solve the game
solved_cases = {}
for i in range(runs):
    # Create the 6x6 game board.
    board = Board(board_size)

    # Create the begin situation.
    A = Vehicle('A', 2, [(1, 2), (1, 3)], 'horizontal')
    B = Vehicle('B', 3, [(1, 4), (1, 5), (1, 6)], 'horizontal')
    C = Vehicle('C', 2, [(2, 2), (2, 3)], 'horizontal')
    D = Vehicle('D', 2, [(2, 4), (3, 4)], 'vertical')
    E = Vehicle('E', 2, [(2, 5), (2, 6)], 'horizontal')
    F = Vehicle('F', 2, [(3, 3), (4, 3)], 'vertical')
    G = Vehicle('G', 2, [(4, 1), (4, 2)], 'horizontal')
    H = Vehicle('H', 2, [(4, 4), (4, 5)], 'horizontal')
    I = Vehicle('I', 2, [(3, 6), (4, 6)], 'vertical')
    J = Vehicle('J', 2, [(5, 1), (6, 1)], 'vertical')
    K = Vehicle('K', 2, [(5, 3), (6, 3)], 'vertical')
    L = Vehicle('L', 2, [(5, 5), (5, 6)], 'horizontal')

    # Create red car
    X = Vehicle('X', 2, [(3, 1), (3, 2)], 'horizontal')

    vehicles = [A, B, C, D, E, F, G, H, I, J, K, L, X]

    # Create the game.
    game = Game(board, vehicles, X)

    # Create a list to track the movements.
    moves = []

    # Move vehicles around randomly until the game is finished.
    tries = 0
    while not game.is_finished():
        # Get a random number of steps.
        steps = 0
        while steps == 0:
            steps = random.randint(-(board_size) - 2, board_size - 2)

        # Get a random vehicle.
        random_vehicle = vehicles[random.randint(0, len(vehicles) - 1)]

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

        tries += 1
        if tries > 100000:
            break

        solved_cases[f"{i}"] = moves

# Calculate runtime  
s = time.time() - start_time
h = s // 3600
s %= 3600
m = s // 60
s %= 60

# Get best result and average moves
first_iter = True
previous_case = None
avg_moves = []
for case in solved_cases:
    avg_moves.append(len(solved_cases[case]))
    if first_iter:
        previous_case = case
        first_iter = False
    if len(solved_cases[case]) < len(solved_cases[previous_case]):
        previous_case = case

# Print results
print(f"Moves: {avg_moves}")
print(f"Runtime: {round(h)} hours, {round(m)} minutes and {round(s)} seconds")
print(f"Runs: {runs}")
print(f"Average moves: {sum(avg_moves) / len(avg_moves)}")
print(f"Least moves: {len(solved_cases[previous_case])}")

# Create output file with best result 
with open('output.csv', 'w+', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(["car", "move"])
    writer.writerows(solved_cases[previous_case])

# TODO: file schrijven met het beste resultaat ooit, of is dat nutteloos?