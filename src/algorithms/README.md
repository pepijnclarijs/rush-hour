## algorithms folder
1. breachbound
2. breadthfirst
3. depthfirst
4. depthfirstbb
5. random
6. heuristics (seperate folder)

To run the algorithms they get called on from the main.py

### random.py
Random algorithm goes through all possible moves without soft constraints.

### breadthfirst.py
Breadth First Search algorithm: Iterates over the entire breadthlevel before proceding to the next depth to find a guaranteed best solution.

### bestfirst.py
Best First Search algorithm:  Iterates over the entire breadthlevel before proceding to the next depth. Sort the depths based on heuristics before proceeding to the next depth. Aventually finds a guaranteed best solution.

### depthfirst.py
Depth First Search algorithm: Iterates over as deep as possible until it hits a dead end and backtracks to a previous unique state with multiple unused moves, that move to other unique states.  

### breachbound
Breach and Bound algorithm:  Iterates over as deep as possible until it hits a dead end or reaches a previously set max depth (bound) and backtracks to a previous unique state with multiple unused moves, that move to other unique states.  

### heuristics
1. def is_exit_reachable(game)
checks if the red car can be moved to the finish.
2. move_trucks_first(game)
checks if by preferring to move trucks instead of cars the game finishes in less moves. (non-operational)
