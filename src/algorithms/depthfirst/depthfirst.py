import copy
from load import load_game

archive = []

def game_in_archive(game_vehicles):
    if len(archive) == 0:
        return_bool = False
    else:
        for arch_vehicles in archive:
            game_equal = True

            for id in game_vehicles.keys():
                if arch_vehicles[id] != vehicles_b[id]:
                    game_equal = False

            if game_equal:
                return True

        return False

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
    def __init__(parent_node, game):
        self.parent = parent_node
        self.game = game

    def traverse_depth(self):
        if self.game.is_finished():
            return []

        if game_in_archive(self.game.vehicles):
            return None

        archive.append(copy.deepcopy(self.game.vehicles))

        for move in self.game.possible_moves:
            child_game = copy.deepcopy(self.game)
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

    def game_in_archive()
