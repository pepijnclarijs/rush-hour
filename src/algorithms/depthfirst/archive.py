class Archive:
    def __init__(self):
        self.archive = []

    def add_board_state(self, vehicle_list):
        self.archive.append(vehicle_list)

    def game_in_archive(self, vehicles):
        if len(self.archive) == 0:
            return_bool = False

        else:
            for arch_vehicles in self.archive:
                board_state_equal = True

                for id in vehicles.keys():
                    if not arch_vehicles[id].equals(vehicles[id]):
                        board_state_equal = False

                if board_state_equal:
                    return True

            return False
