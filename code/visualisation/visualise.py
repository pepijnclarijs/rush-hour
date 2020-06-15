from tkinter import Tk, Label

import random 
import time

from load import load_game

def visualise(game, result, board_size):

    root = Tk()
    root.title("Rush Hour")
    root.geometry('700x700')
    root.configure(bg='grey')

    boxes = {}
    for row in range(1, board_size+1):
        for col in range(1, board_size+1):
            box = Label(root, text=f'{row},{col}', bg='white', bd=40)
            box.grid(column=col, row=row)
            boxes[(row, col)] = box

    for vehicle in game.vehicles:
        vehicle_color = ["#"+''.join([random.choice('0123456789ABCDEF') for j in range(6)])]
        print(vehicle)
        for position in vehicle.position:
            print(position)
            boxes[position].configure(background=vehicle_color)      

    # print(result)
    # for move in result['0']:
    #     time.sleep(1)
    #     print(move)

    root.mainloop() 