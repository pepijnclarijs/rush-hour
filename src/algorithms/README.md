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
Breadth First Search algorithm: Iterates over the entire depthlevel before proceding to the next to find a guaranteed best solution.

### depthfirst.py
Depth First Search algorithm: Iterates over as deep as possible until it hits a dead end and backtracks to a previous unique state with multiple unused moves, that move to other unique states.  

### depthfirstbb

### breachbound

### heuristics
1. def is_exit_reachable(game)
checks if the red car can be moved to the finish.
2. move_trucks_first(game)
checks if by preferring to move trucks instead of cars the game finishes in less moves. (non-operational)
