def move_trucks_first(game)

truck = game.vehicle.size(3)

# for vehicle in self.vehicles.values():
#     # if truck in
#     for move in self.game.possible_moves:

if game.validate_move(truck, game.move(vehicle, new_pos)):
    return True

return False
