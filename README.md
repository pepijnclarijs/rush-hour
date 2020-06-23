# A rush-hour Constraint Optimisation Problem BY **TEAM ONLY RUSH!!!**
gebruik/installatie/introductie van de case
Objective: Solve the rush hour game as efficiently possible.

General goal of the game:
Get the red car off the board in one straight line.
The vehicles on the gameboard must be moved in such a way that the red car can leave.

## To run the code
** Use commandline arguments **
example: python main.py -g 3 -s 6 -a random -d 30 -v
example run: game3.csv of board_size 6 with algorithm random.py with a max depth of 30 and display visualisation.
- '-g' '--game_number' add int
- '-s' '--size' add int
- '-a', '--algorithm' add _some_algorithm_.py
- '-e','--exit_reachable'
- '-u','--state_unique'
- '-i','--iterations' add int
- '-m','--max_runs' add int
- '-d','--depth' add int
- '-v','--visualisation' 

Results printed after running:
The Results are calculated by number of moves, time it takes to run the code, number of moves, average number of moves when iterating over the game for multiple rounds.
