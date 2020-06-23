import copy, random

from src.util import finish_game
from src.heuristics.heuristics import is_exit_reachable
from src.heuristics.heuristics import is_state_unique


def randomize(init_game, iterations, state_unique, exit_reachable, board_size, max_tries):
    """
    Moves vehicles around at random until the game is solved.

    Args:
        init_game (Game): The initial game instance.
        board_size (int): Integer that represents the length and width of the board.
        iterations (int): Integer that indicates the number of times the game should be solved.
        max_tries (int): The number of times the program should try to move a vehicle.

    Returns:
        List of tuples containing a string representing the id of a vehicle and an integer representing the number of
        steps [('A', 2), ('B', -2)]. The list represents the movements that should be executed to solve the game.
    """
    solved_cases = {}
    for i in range(iterations):
        # Process counter
        print(f'Processing... Iteration number: {i}')

        # Load game
        game = copy.deepcopy(init_game)

        # Create a list to track the movements.
        moves = []

        # Track the states.
        seen_states = []
        seen_states.append(game.current_state)

        # Move vehicles around randomly until the game is finished.
        tries = 0
        tries_until_stuck = 0

        while not game.is_finished():
            # From the possible moves, pick a random move.
            random_move = random.choice(list(game.possible_moves))
            random_vehicle = random_move[0]
            steps = random_move[1]
            new_coordinates = random_vehicle.speculate_new_position(steps)

            # Heuristic: check if the movement results in a unique state.
            if state_unique == True:
                speculated_game = copy.deepcopy(game)
                vehicle_in_speculated_game = speculated_game.vehicles.get(random_vehicle.id)
                speculated_game.move(vehicle_in_speculated_game, new_coordinates)
                speculated_state = speculated_game.current_state
                if not is_state_unique(seen_states, speculated_state):
                    tries_until_stuck += 1
                    if tries_until_stuck > 20:
                        print("Got stuck :( ")
                        moves.clear()
                        break
                    continue
                tries_until_stuck = 0

                # Save the state.
                seen_states.append(speculated_state)

            # Move the vehicle to the new position.
            game.move(random_vehicle, new_coordinates)

            # Save the movements of the vehicles.
            move = (random_vehicle.id, steps)
            moves.append(move)

            # Do not try more than max_tries moves.
            tries += 1
            if tries > max_tries:
                print("max tries exceeded")
                break

            # Heuristic: check if the red car can be moved to the exit.
            if exit_reachable == True:
                if is_exit_reachable(game):
                    last_move = finish_game(game)
                    moves.append(last_move)

        if moves:
            print('Found exit!')
            solved_cases[i] = moves

    return solved_cases, game.vehicles
