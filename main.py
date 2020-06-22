from src.algorithms.random import random
from src.algorithms.breadthfirst import breadthfirst
from src.algorithms.depthfirst import depthfirst, archive
from src.algorithms.depthfirst.archive import Archive
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
        if game_number <= 3:
            board_size = 6
        elif game_number > 3:
            board_size = 9
        elif game_number == 7:
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
        archive = Archive()
        rootnode = depthfirst.Depthfirst(None, init_game, archive)
        results = rootnode.traverse_depth()
        results.reverse()
        
        print(results)

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
    print(results)
    for result in results:
        avg_moves.append(len(results[result]))
        if len(results[result]) < len(best_result):
            best_result = results[result]

    # Create visualisation
    if visualisation == True:
        vis.visualise(init_game, best_result, board_size)

    # Print results
    print(f"Moves: {avg_moves}")
    print(f"Runtime: {round(h)} hours, {round(m)} minutes and {round(s)} seconds")
    print(f"Iterations: {iterations}")
    print(f"Average moves: {round(sum(avg_moves) / len(avg_moves))}")
    print(f"Least moves: {len(best_result)}")

    # Check best result
    with open(f"data/results/{algorithm}/game#{game_number}/game{game_number}_best_run.csv", 'w+') as f:
        best_stat = f.readline()

    if best_stat and int(best_stat) >= len(best_result):
        with open(f"data/results/{algorithm}/game#{game_number}/game{game_number}_best_run.csv", 'w+', newline='') as f:
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
    with open(f"data/results/{algorithm}/game#{game_number}/game{game_number}_results.csv", 'a+', newline='') as f:
        writer = csv.writer(f)
        if f.tell() == 0:
            writer.writerow(['least', 'average', 'iterations', "runtime(sec)"])
        writer.writerow([len(best_result), round(sum(avg_moves) / len(avg_moves)), iterations, round(seconds)])


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-g', '--game_number', type=int, required=True, help='Choose game number')
    parser.add_argument('-s', '--size', type=int, required=False, default=-1, help='The width and height of the board')
    parser.add_argument('-a', '--algorithm', type=str, choices=['random', 'bf', 'df'], required=True, help='Choose algorithm')
    parser.add_argument('-i','--iterations', type=int, required=False, default=1, help='Enter amount of iterations')
    parser.add_argument('-d','--depth', type=int, required=False, default=30, help='Enter depth')
    parser.add_argument('-v','--visualisation', action="store_true", help='Generate visualisation')

    args = parser.parse_args()
    run(args.game_number, args.size, args.algorithm, args.iterations, args.depth, args.visualisation)
