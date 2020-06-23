## classes folder
1. class Game
2. class Board
3. class Vehicle
4. class Depthfirst

### class Game
Takes in arguments for self, board & vehicles.
Vehicle moves are are made from here.
The game checks for possible moves list from the coordinate values given in the vehicles dictionary of the current state of the game.


### class board
Takes in arguments for self & length.
Finds the correct box for the red_car to exit and finish the game.

### class vehicle
Takes in arguments for id, position & color.
Calcute how the vehicles move on the grid here.
- individual boxes on the grid can be passed and return the final or end position of the vehicle that was moved.
Check if state of child node is equal to a previous node in the archive.

### class Depthfirst (in algorithms folder)
Takes in parent_node, game, archive & max_depth.
traverse_depth of the rush hour game tree and check for unique states in the child nodes with class Archive
