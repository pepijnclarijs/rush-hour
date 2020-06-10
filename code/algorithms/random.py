import random
import sys

from load import load_game

# Start game 
def randomize(board_size, runs):
    solved_cases = {}

    for i in range(runs):
        # Load new game
        game = load_game(board_size)
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
            random_vehicle = game.vehicles[random.randint(0, len(game.vehicles) - 1)]

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
        
    return solved_cases     