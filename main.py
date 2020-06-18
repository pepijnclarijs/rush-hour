from src.algorithms import random
from src.algorithms.breadthfirst import breadthfirst
from src.visualisation import visualise as vis

# tijdelijk voor testen:
from bf import breadth

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
    depth = 23

    print(f"Playing game {game_number}, with board size {board_size}, for {runs} runs")

    # print("Playing " + sys.argv[1])
    #
    # initial_board = sys.argv[1]
    # runs = int(sys.argv[2])
    # # size_and_num = initial_board[8:-4] # 6x6_1
    # board_size = int(size_and_num.split('_')[0].split('x')[0])
    # game_number = int(size_and_num.split('_')[1])

    # Set start time for performence measurements
    start_time = time.time()

    # Load game
    init_game = load_game(game_number, board_size)

    # Solve the game with random
    # results = random.randomize(init_game, runs, board_size)
    
    # Solve the game with breadthfirst
    results = breadthfirst.breadth_first(init_game, runs, depth)

    # # Solve the game with deapthdirst
    # rootnode = Depthfirst(None, init_game)

    # Calculate runtime
    s = time.time() - start_time
    seconds = s
    h = s // 3600
    s %= 3600
    m = s // 60
    s %= 60

    # Get best result and average moves
    avg_moves = []
    best_result = results[0]
    for result in results:
        avg_moves.append(len(results[result]))
        if len(results[result]) < len(best_result):
            best_result = results[result]   

    # Create visualisation
    vis.visualise(init_game, best_result, board_size)

    # Print results
    print(f"Moves: {avg_moves}")
    print(f"Runtime: {round(h)} hours, {round(m)} minutes and {round(s)} seconds")
    print(f"Runs: {runs}")
    print(f"Average moves: {round(sum(avg_moves) / len(avg_moves))}")
    print(f"Least moves: {len(best_result)}")

    # Check best result
    with open(f"data/game#{game_number}/game{game_number}_best_run.csv", 'r') as f:
        best_stat = f.readline()

    # Overwrite if best result
    if int(best_stat) >= len(best_result):
        with open(f"data/game#{game_number}/game{game_number}_best_run.csv", 'w+', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([len(best_result)])
            writer.writerow([f"Runtime: {round(h)} hours, {round(m)} minutes and {round(s)} seconds"])
            writer.writerow([f"Runs: {runs}"])
            writer.writerow([f"Average moves: {sum(avg_moves) / len(avg_moves)}"])
            writer.writerow([f"Least moves: {len(best_result)}"])
            writer.writerow([f"Moves: {avg_moves}"])
            writer.writerow(["car", "move"])
            writer.writerows(best_result)

    # Append results
    with open(f"data/game#{game_number}/game{game_number}_results.csv", 'a', newline='') as f:
        writer = csv.writer(f)
        if f.tell() == 0:
            writer.writerow(['least', 'average', 'runs', "runtime(sec)"])
        writer.writerow([len(best_result), round(sum(avg_moves) / len(avg_moves)), runs, round(seconds)])
