from code.algorithms import random

import csv
import time

if __name__ == "__main__":
    # set amount of runs
    runs = 1
    board_size = 6
    game_number = "4"

    # set start time for performence measurements
    start_time = time.time()

    # Solve the game with random
    result = random.randomize(board_size, runs)

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
    for case in result:
        avg_moves.append(len(result[case]))
        if first_iter:
            previous_case = case
            first_iter = False
        if len(result[case]) < len(result[previous_case]):
            previous_case = case

    # Print results
    print(f"Moves: {avg_moves}")
    print(f"Runtime: {round(h)} hours, {round(m)} minutes and {round(s)} seconds")
    print(f"Runs: {runs}")
    print(f"Average moves: {sum(avg_moves) / len(avg_moves)}")
    print(f"Least moves: {len(result[previous_case])}")

    # Check best result
    with open(f"data/game#{game_number}/game#{game_number}_best_run.csv", 'r') as f:
        # reader = csv.reader(f)
        best_result = f.readline()

    # Overwrite if best result
    if int(best_result) >= len(result[previous_case]):
        with open(f"data/game#{game_number}/game#{game_number}_best_run.csv", 'w+', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([len(result[previous_case])])
            writer.writerow([f"Runtime: {round(h)} hours, {round(m)} minutes and {round(s)} seconds"])
            writer.writerow([f"Runs: {runs}"])
            writer.writerow([f"Average moves: {sum(avg_moves) / len(avg_moves)}"])
            writer.writerow([f"Least moves: {len(result[previous_case])}"])
            writer.writerow([f"Moves: {avg_moves}"])
            writer.writerow(["car", "move"])
            writer.writerows(result[previous_case])

