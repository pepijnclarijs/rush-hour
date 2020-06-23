import argparse, csv, sys, time

from src.algorithms.random import random
from src.algorithms.breadthfirst import breadthfirst
from src.algorithms.bestfirst import bestfirst
from src.algorithms.depthfirst import depthfirst, archive
from src.algorithms.depthfirst.archive import Archive
from src.algorithms.breachbound import breachbound
from src.load import load_game
from src.visualisation import visualise as vis


def run(game_number, game_size, algorithm, exit_reachable, state_unique, iterations, max_tries, depth, visualisation):
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
        results, winning_game = random.randomize(init_game, iterations, state_unique, exit_reachable, board_size, max_tries)
    elif algorithm == 'bf':
        results = breadthfirst.breadthfirst(init_game)
    elif algorithm == 'bffs':
        with open(f"data/boards/game{game_number}_winning_state.csv", 'r') as f:
            reader = csv.reader(f)
            winning_state = dict(reader)    
        winning_state = {'A': [(1, 1), (1, 2)], 'B': [(1, 3), (1, 4), (1, 5)], 'C': [(2, 1), (2, 2)], 'D': [(2, 4), (2, 5)], 'E': [(5, 4), (4, 4)], 'F': [(4, 1), (4, 2)], 'G': [(3, 3), (2, 3)], 'H': [(4, 5), (4, 6)], 'I': [(2, 6), (1, 6)], 'J': [(5, 5), (5, 6)], 'K': [(6, 1), (5, 1)], 'L': [(5, 3), (4, 3)], 'X': [(3, 5), (3, 6)]}    
        results = bestfirst.bestfirst(init_game, exit_reachable, state_unique, winning_state)        
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
    elif algorithm == 'bb':
        results = breachbound.breachbound(init_game, depth, exit_reachable, state_unique)
    else:
        sys.exit('Cannot find algorithm')

    if not results:
        sys.exit('No results found..')

    # Calculate runtime
    s = time.time() - start_time
    seconds = s
    h = s // 3600
    s %= 3600
    m = s // 60
    s %= 60

    # Get solved times for random + heuristic: unique state
    if algorithm == 'random' and state_unique == True:
        solved_times = 0 
        for result in results:
            if len(results[result]) == 1:
                continue
            solved_times += 1

    # Get best result and average moves
    avg_moves = []

    print(results)
    if algorithm == 'random':
        first_result = iterations +1 - solved_times 
        # best_result = results[first_result]
        
        # dit weg bovenstaand eregel uncomment
        best_result = []
        for i in range(9999):
            best_result.append(i)
    else:
        best_result = results[0]
    for result in results:
        avg_moves.append(len(results[result]))
        if len(results[result]) < len(best_result):
            best_result = results[result]
        
    # Create visualisation
    if visualisation:
        game = load_game(game_number, board_size)
        vis.visualise(game, best_result, board_size)

    # Print results
    print(f"Amount of moves to reach exit per game: {avg_moves}")
    print(f"Runtime: {round(h)} hours, {round(m)} minutes and {round(s)} seconds")
    print(f"Iterations: {iterations}")
    print(f"Average moves to reach exit: {round(sum(avg_moves) / len(avg_moves))}")
    print(f"Least moves to reach exit: {len(best_result)}")
    if algorithm == 'random' and state_unique == True:
        print(f"{(solved_times/iterations) * 100}% of the games was solved.") 
 

    # Fix result saving name problems
    heuristics = 'no_heuristics'
    if state_unique or exit_reachable:
        heuristics = 'heuristics'
    if algorithm == 'bf':
        algorithm = 'breadthfirst' 
    if algorithm == 'bffs':
        algorithm = 'bestfirst' 
    elif algorithm == 'df':
        algorithm = 'depthfirst'
    elif algorithm == 'bb':  
        algorithm = 'breachbound'
    
    # Check best result
    with open(f"data/results/{algorithm}/{heuristics}/game#{game_number}/game{game_number}_best_run.csv", 'w+', newline='') as f:
        best_stat = f.readline()
    if best_stat == '':
        best_stat = float('inf')

    if best_stat >= len(best_result):
        with open(f"data/results/{algorithm}/{heuristics}/game#{game_number}/game{game_number}_best_run.csv", 'w+', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([len(best_result)])
            writer.writerow([f"Runtime: {round(h)} hours, {round(m)} minutes and {round(s)} seconds"])
            writer.writerow([f"Iterations: {iterations}"])
            writer.writerow([f"Average moves: {sum(avg_moves) / len(avg_moves)}"])
            writer.writerow([f"Least moves: {len(best_result)}"])
            writer.writerow([f"Moves: {avg_moves}"])
            writer.writerow([f"Heuristic is state unique enabled: {state_unique}"])
            writer.writerow([f"Heuristic is exit reachable enabled: {exit_reachable}"])    
            writer.writerow(["car", "move"])
            writer.writerows(best_result)

        # Add winning state with least moves for best first
        with open(f"data/boards/game{game_number}_winning_state.csv", 'w+', newline='') as f:    
            for vehicle, position in winning_game.items():
                writer = csv.writer(f)
                writer.writerow([vehicle, position])

    # Append results
    with open(f"data/results/{algorithm}/{heuristics}/game#{game_number}/game{game_number}_results.csv", 'a+', newline='') as f:
        writer = csv.writer(f)
        if f.tell() == 0:
            writer.writerow(['least', 'average', 'iterations', 'runtime(sec)', ' is state unique', 'is exit reachable'])
        writer.writerow([len(best_result), round(sum(avg_moves) / len(avg_moves)), iterations, round(seconds), state_unique, exit_reachable])

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-g', '--game_number', type=int, required=True, help='Choose game number')
    parser.add_argument('-s', '--size', type=int, required=False, default=-1, help='The width and height of the board')
    parser.add_argument('-a', '--algorithm', type=str, choices=['random', 'bf', 'bffs', 'df','bb'], required=True, help='Choose algorithm')
    parser.add_argument('-e','--exit_reachable', action="store_false", help='Disable heuristic: exit_reachable')
    parser.add_argument('-u','--state_unique', action="store_false", help='Disable heuristic: state_unique')    
    parser.add_argument('-i','--iterations', type=int, required=False, default=1, help='Enter amount of iterations')
    parser.add_argument('-m','--max_runs', type=int, required=False, default=10000, help='Change max runs for random algorithm, default: 10000')
    parser.add_argument('-d','--depth', type=int, required=False, default=30, help='Enter depth')
    parser.add_argument('-v','--visualisation', action="store_true", help='Generate visualisation')

    args = parser.parse_args()
    run(args.game_number, args.size, args.algorithm, args.exit_reachable, args.state_unique, args.iterations, args.max_runs, args.depth, args.visualisation)
