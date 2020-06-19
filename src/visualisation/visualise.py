from tkinter import Tk, Label, Button

import random 
import time


def visualise(init_game, result, board_size):
    root = Tk()
    root.title("Rush Hour")
    root.geometry('700x700')
    root.configure(bg='grey')

    counter = 0
    speed = 0.01
    if len(result) < 40:
        speed = 1

    boxes = {}
    for row in range(1, board_size+1):
        for col in range(1, board_size+1):
            box = Label(root, text=f'{row},{col}', bg='white', bd=40)
            box.grid(row=row, column=col)
            boxes[(row, col)] = box

    for vehicle in init_game.vehicles.values():
        if vehicle.id != 'X':
            vehicle.color = ["#"+''.join([random.choice('0123456789ABCDEF') for j in range(6)])]
        else:
            vehicle.color = "red"    
        for position in vehicle.get_position():
            boxes[position].configure(background=vehicle.color)   

    def start():   
        for move in result:       
            time.sleep(speed)
            counter=+1
            vehicle = init_game.vehicles[move[0][0]]
            for position in vehicle.position:
                    boxes[position].configure(background='white')
            # vehicle.set_position(vehicle.speculate_new_position(move[1]))


            new_coordinates = vehicle.speculate_new_position(move[1])

            if init_game.validate_move(vehicle, new_coordinates):
                init_game.move(vehicle, new_coordinates)

            for position in vehicle.position:
                boxes[position].configure(background=vehicle.color)
            root.update()

    startbtn = Button(root, text='Start', command=start).grid() 

    root.mainloop()
            

       

        