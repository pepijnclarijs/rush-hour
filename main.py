from code.algorithms import random

import csv
import time

# set amount of runs
runs = 3
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

# Create output file with best result
with open('output.csv', 'w+', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(["car", "move"])
    writer.writerows(result[previous_case])

# TODO: file schrijven met het beste resultaat ooit, of is dat nutteloos?
