from src.algorithms import random
from src.algorithms import breadth_first
from src.visualisation import visualise as vis

from load import load_game

import csv
import time
import sys

if __name__ == "__main__":
    # set amount of runs
    """ command line arguments for game_number, board_size & runs """
    game_number = sys.argv[1]
    board_size = int(sys.argv[2])
    runs = int(sys.argv[3])

    print(f"Playing game {game_number}, with board size {board_size}, for {runs} runs")

    # print("Playing " + sys.argv[1])
    #
    # initial_board = sys.argv[1]
    # runs = int(sys.argv[2])
    # # size_and_num = initial_board[8:-4] # 6x6_1
    # board_size = int(size_and_num.split('_')[0].split('x')[0])
    # game_number = int(size_and_num.split('_')[1])

    # set start time for performence measurements
    start_time = time.time()

    # Load game
    init_game = load_game(game_number, board_size)

    # Solve the game with random
    result = random.randomize(game_number, runs, board_size)
    result = breadth_first.breadth_first()

    # Calculate runtime
    s = time.time() - start_time
    seconds = s
    h = s // 3600
    s %= 3600
    m = s // 60
    s %= 60

    """ Create visualisation """
    # vis.visualise(init_game, result, board_size)

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
    print(f"Average moves: {round(sum(avg_moves) / len(avg_moves))}")
    print(f"Least moves: {len(result[previous_case])}")

    # Check best result
    with open(f"data/game#{game_number}/game{game_number}_best_run.csv", 'r') as f:
        best_result = f.readline()

    # Overwrite if best result
    if int(best_result) >= len(result[previous_case]):
        with open(f"data/game#{game_number}/game{game_number}_best_run.csv", 'w+', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([len(result[previous_case])])
            writer.writerow([f"Runtime: {round(h)} hours, {round(m)} minutes and {round(s)} seconds"])
            writer.writerow([f"Runs: {runs}"])
            writer.writerow([f"Average moves: {sum(avg_moves) / len(avg_moves)}"])
            writer.writerow([f"Least moves: {len(result[previous_case])}"])
            writer.writerow([f"Moves: {avg_moves}"])
            writer.writerow(["car", "move"])
            writer.writerows(result[previous_case])

    # Append results
    with open(f"data/game#{game_number}/game{game_number}_results.csv", 'a', newline='') as f:
        writer = csv.writer(f)
        if f.tell() == 0:
            writer.writerow(['least', 'average', 'runs', "runtime(sec)"])
        writer.writerow([len(result[previous_case]), round(sum(avg_moves) / len(avg_moves)), runs, round(seconds)])
