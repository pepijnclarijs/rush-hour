from src.algorithms.random import random
from src.algorithms.breadthfirst import breadthfirst
from src.algorithms.depthfirst import depthfirst, archive
from src.algorithms.depthfirst.archive import Archive
from src.algorithms.depthfirstbb import depthfirstbb
from src.algorithms.depthfirstbb import depthfirstbb2
from src.algorithms.depthfirstbb import depthfirstbbr
from src.algorithms.depthfirstbb import depthfirstbbr2
from src.visualisation import visualise as vis

from src.load import load_game

import argparse
import csv
import time
import sys

def run(game_number, game_size, algorithm, iterations, depth, visualisation):
    """ command line arguments for game_number, board_size & iterations """

    if game_size > 0:
        board_size = game_size
    else:
        if game_number < 4:
            board_size = 6
        elif game_number < 7:
            board_size = 9
        else:
            board_size = 12

    print(f"Playing game {game_number}, with board size {board_size}, for {iterations} iterations with {algorithm} algorithm")

    # Set start time for performence measurements
    start_time = time.time()

    # Load game
    init_game = load_game(game_number, board_size)

    if algorithm == 'random':
        results = random.randomize(init_game, iterations, board_size)
    elif algorithm == 'bf':
        results = breadthfirst.breadthfirst(init_game)
    elif algorithm == 'df':
        results = []
        for i in range(depth):
            print(i)
            archive = Archive()
            rootnode = depthfirst.Depthfirst(None, init_game, archive, i)
            result_moves = rootnode.traverse_depth(0)
            if result_moves is not None:
                result_moves.reverse()
            results.append(result_moves)
            print(result_moves)
    elif algorithm == 'dfbb':
        results = depthfirstbb.depthfirstbb(init_game, depth)
    elif algorithm == 'dfbbr':
        results = depthfirstbbr.depthfirstbbr(init_game, depth)
    else:
        print("Error running algorithm")

        print(results)
        print(f"number of moves df: {len(results)}")

    # Calculate runtime
    s = time.time() - start_time
    seconds = s
    h = s // 3600
    s %= 3600
    m = s // 60
    s %= 60

    # Get best result and average moves
    avg_moves = []
    best_result = results[0] # TODO: uncomment later
    # best_result = [] # TODO: del this
    # for stupid in range(90000): # TODO del this for loop
    #     best_result.append(stupid)
    # solved_times = 0 # TODO: delete later. just for random + heuristic: unique state.
    # for result in results:
    #     # # TODO: delete later. just for random + heuristic: unique state.
    #     # if len(results[result]) == 1:
    #     #     continue
    #     # solved_times += 1
    #     # # ENDTODO
    #
    #     avg_moves.append(len(results[result]))
    #     if len(results[result]) < len(best_result):
    #         best_result = results[result]
    #
    # print(best_result)

    # Create visualisation
    if visualisation:
        game = load_game(game_number, board_size)
        vis.visualise(game, best_result, board_size)

    # Print results
    print(f"Moves: {avg_moves}")
    print(f"Runtime: {round(h)} hours, {round(m)} minutes and {round(s)} seconds")
    print(f"Iterations: {iterations}")
    print(f"Average moves: {round(sum(avg_moves) / len(avg_moves))}")
    print(f"Least moves: {len(best_result)}")
    # print(f"{(solved_times/iterations) * 100}% of the games was solved.") # TODO: del later. just for random + heuristic: unique state.
    #
    # Check best result
    with open(f"data/results/random/no_heuristics/game#{game_number}/game{game_number}_best_run.csv", 'w+') as f:
        best_stat = f.readline()

    # Overwrite if best result. Create if this is the first result.
    first_result = True
    if len(best_stat) != 0:
        first_result = False
    else:
        best_stat = '0'

    if int(best_stat) >= len(best_result) or first_result: #or int(best_stat) != len(best_restult):
        with open(f"data/results/random/no_heuristics/game#{game_number}/game{game_number}_best_run.csv", 'w+', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([len(best_result)])
            writer.writerow([f"Runtime: {round(h)} hours, {round(m)} minutes and {round(s)} seconds"])
            writer.writerow([f"Iterations: {iterations}"])
            writer.writerow([f"Average moves: {sum(avg_moves) / len(avg_moves)}"])
            writer.writerow([f"Least moves: {len(best_result)}"])
            writer.writerow([f"Moves: {avg_moves}"])
            writer.writerow(["car", "move"])
            writer.writerows(best_result)

    # Append results
    with open(f"data/results/random/no_heuristics/game#{game_number}/game{game_number}_results.csv", 'a+', newline='') as f:
        writer = csv.writer(f)
        if f.tell() == 0:
            writer.writerow(['least', 'average', 'iterations', "runtime(sec)"])
        writer.writerow([len(best_result), round(sum(avg_moves) / len(avg_moves)), iterations, round(seconds)])
        #writer.writerow([f"{(solved_times / iterations) * 100}% of the games was solved."])  # TODO:


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-g', '--game_number', type=int, required=True, help='Choose game number')
    parser.add_argument('-s', '--size', type=int, required=False, default=-1, help='The width and height of the board')
    parser.add_argument('-a', '--algorithm', type=str, choices=['random', 'bf', 'df','dfbb', 'dfbbr','dfbb2', 'dfbbr2'], required=True, help='Choose algorithm')
    parser.add_argument('-i','--iterations', type=int, required=False, default=1, help='Enter amount of iterations')
    parser.add_argument('-d','--depth', type=int, required=False, default=30, help='Enter depth')
    parser.add_argument('-v','--visualisation', action="store_true", help='Generate visualisation')

    args = parser.parse_args()
    run(args.game_number, args.size, args.algorithm, args.iterations, args.depth, args.visualisation)
