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
        in REVERSE order. So in order to use the move list they get reversed first.
    Usage:
        game = Depthfirst(None, initial_game, archive, max_depth)
        result_moves --> reverse()

    """
    def __init__(self, parent_node, game, archive):
    # def __init__(self, parent_node, game, archive, max_depth):
        self.parent = parent_node
        self.game = game
        self.archive = archive
        # self.max_depth = max_depth
        #
        # print("Current state:")
        # game.print_board()
        # print("")


    def traverse_depth(self):
        if is_exit_reachable(self.game):
            return_moves = []
            last_move = finish_game(self.game)
            actual_move = self.game.vehicles[last_move[0]].speculate_new_position(last_move[1])
            return_moves.append(last_move)
            return return_moves

        if self.archive.game_state_in_archive(self.game.vehicles):
            return None

        self.archive.add_board_state(copy.deepcopy(self.game.vehicles))

        for move in self.game.possible_moves:
            child_game = copy.deepcopy(self.game)
            (vehicle, steps) = move
            new_pos = vehicle.speculate_new_position(steps)
            child_game.move(child_game.vehicles[vehicle.id], new_pos)

            child_node = Depthfirst(self, child_game, self.archive)
            traversal_list = child_node.traverse_depth()
            # print(traversal_list)
            if traversal_list is not None:
                traversal_list.append((vehicle.id, steps))
                return traversal_list

        return None
    # def traverse_depth(self, depth):
    #     print(depth)
    #     if depth >= self.max_depth:
    #         return None
    #
    #     if is_exit_reachable(self.game):
    #         return_moves = []
    #         last_move = finish_game(self.game)
    #         actual_move = self.game.vehicles[last_move[0]].speculate_new_position(last_move[1])
    #         return_moves.append(actual_move)
    #         return return_moves
    #     #print("exit not reachable")
    #
    #     if self.archive.game_state_in_archive(self.game.vehicles):
    #         return None
    #
    #     self.archive.add_board_state(copy.deepcopy(self.game.vehicles))
    #
    #     for move in self.game.possible_moves:
    #         child_game = copy.deepcopy(self.game)
    #         (vehicle, steps) = move
    #         new_pos = vehicle.speculate_new_position(steps)
    #         child_game.move(child_game.vehicles[vehicle.id], new_pos)
    #
    #         child_node = Depthfirst(self, child_game, self.archive, self.max_depth)
    #         next_depth = depth + 1
    #         traversal_list = child_node.traverse_depth(next_depth)
    #         # print(traversal_list)
    #         if (traversal_list is not None):
    #             traversal_list.append((vehicle.id, steps))
    #             return traversal_list




        # Een lijst aan 'child' games, met ieder één van de
        # mogelijk uit te voeren moves.

        #   Game -> mogelijke moves
        #   list game (deepcopy)
        #   vehicles
        #       speculated moves

        # lijst games
        # length: mogelijke moves
        # mogelijke move[i] uitvoeren op game[i]
