import copy, sys
# from sys import recursionlimit
from src.algorithms.depthfirst.archive import Archive
from src.heuristics.heuristics import is_exit_reachable
from src.util import finish_game
from src.load import load_game

sys.setrecursionlimit(10**6)

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
            return_moves = []
            # This move needs to be the same type as the moves
            # from possible_moves
            last_move = finish_game(self.game)
            print("Last move: " + str(last_move))
            actual_move = self.game.vehicles[last_move[0]].speculate_new_position(last_move[1])
            return_moves.append(actual_move)
            print(return_moves)
            return return_moves
        print("Exit not reachable")

        if self.archive.game_in_archive(self.game.vehicles):
            return None
        print("Game not in Archive")

        self.archive.add_board_state(copy.deepcopy(self.game.vehicles))

        for move in self.game.possible_moves:
            child_game = copy.deepcopy(self.game)
            (vehicle, steps) = move
            new_pos = vehicle.speculate_new_position(steps)
            child_game.move(child_game.vehicles[vehicle.id], new_pos)

            child_node = Depthfirst(self, child_game, self.archive)
            traversal_list = child_node.traverse_depth()
            # print(traversal_list)
            if (traversal_list is not None):
                traversal_list.append(move)
                return traversal_list

        return None

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
