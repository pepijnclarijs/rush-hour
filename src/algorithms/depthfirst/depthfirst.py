import copy, sys
from src.algorithms.depthfirst.archive import Archive
from src.heuristics.is_exit_reachable import is_exit_reachable
from src.util import finish_game
from load import load_game

class Depthfirst:
    """
    This class represents a node in the game tree.

    Args:
        parent: The parent game object (None for root node)
        game: The game represented in this game

    Return:
        The list returned contains the moves needed to complete the game,
        in REVERSE order. So in order to use the move list, please REVERSE
        first.

    Usage:
        game = Depthfirst(None, initial_game)
        rev_moveset = game.traverse_depth()
        finish_moves = rev_moveset.reverse()

    """
    def __init__(self, parent_node, game, archive):
        self.parent = parent_node
        self.game = game
        self.archive = archive

        print("Current state:")
        game.print_board()
        print("")

    def traverse_depth(self):
        if is_exit_reachable(self.game):
            last_move = finish_game(self.game)
            return [last_move]

        if self.archive.game_in_archive(self.game.vehicles):
            return None

        self.archive.add_board_state(copy.deepcopy(self.game.vehicles))

        for move in self.game.possible_moves:
            child_game = copy.deepcopy(self.game)
            (vehicle, steps) = move
            new_pos = vehicle.speculate_new_position(steps)
            # child_vehicle = child_game.vehicles.get(vehicle.id)
            child_game.move(vehicle, new_pos)

            child_node = Depthfirst(self, child_game, self.archive)
            traversal_list = child_node.traverse_depth()
            if (traversal_list != None):
                return traversal_list.append(move)
                # child_vehicle = child_game.vehicles.get(vehicle.id)

        return None
            #### okay hoe verder

#### ------ Verdelen over code

        # What we need:
        # Een lijst aan 'child' games, met ieder één van de
        # mogelijk uit te voeren moves.
        # Aanmaken in de constructor

        #
        #   Game -> mogelijke moves
        #   list game (deepcopy)
        #   vehicles
        #       speculated moves
        #   validate move -> bool
        #   move (veh, pos) -> game

        # lijst mogelijke moves
        #   vehicles
        #       speculated moves
        #   validate move
        #       True: move to list

        # lijst games
        # length: mogelijke moves
        # mogelijke move[i] uitvoeren op game[i]
