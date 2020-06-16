import random
import sys
import csv

from load import load_game

# Start game
def randomize(game_number, runs, board_size):
    """
    Moves vehicles around at random until the game is solved.

    Args:
        board_size: Integer that represents the length and width of the board.
        runs: Integer that indicates the number of times the game should be solved.

    Returns:
        List of tuples containing a string representing the id of a vehicle and an integer representing the number of
        steps [('A', 2), ('B', -2)]. The list represents the movements that should be executed to solve the game.
    """
    solved_cases = {}
    for i in range(runs):
        # Load new game
        game = load_game(game_number, board_size)

        # Create a list to track the movements.
        moves = []

        # Move vehicles around randomly until the game is finished.
        tries = 0
        while not game.is_finished():
            # Get a random vehicle
            random_vehicle = random.choice(game.vehicles)

            # Get a random number of steps.
            steps = 0
            while steps == 0:
                steps = random.randint(-board_size - 2, board_size - 2)

            # Speculate the new position passed by the vehicle.
            new_coordinates = random_vehicle.speculate_new_position(steps)

            # Check if the new position is free.
            if game.validate_move(random_vehicle, new_coordinates):
                # Move the vehicle to the new position.
                game.move(random_vehicle, new_coordinates)

                # Save the movements of the vehicles.
                move = (random_vehicle.id, steps)
                moves.append(move)

            tries += 1
            if tries > 100000:
                break

        solved_cases[f"{i}"] = moves
            
    return solved_cases
