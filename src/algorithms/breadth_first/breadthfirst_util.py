# Maybe this is not the way to go. Maybe use game instances correctly. Depends on how much memory it costs.

# def possible_moves_in_state(state, board_size):
#
#     # Get the vehicles from the state.
#     for vehicle_id in state:
#
#
#     for vehicle in self.vehicles:
#         # Get the possible moves in the current state.
#         for steps in range(-self.board.length + vehicle.size, self.board.length - vehicle.size):
#             if steps == 0:
#                 continue
#             new_coordinates = vehicle.speculate_new_position(steps)
#             if self.validate_move(vehicle, new_coordinates):
#                 move = (vehicle, steps)
#                 self.possible_moves.add(move)
#
# def get_vehicle(id):
