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
    for y in range(1, board_size+1):
        for x in range(1, board_size+1):
            box = Label(root, text=f'{y},{x}', bg='white', bd=40)
            box.grid(row=y, column=x)
            boxes[(y, x)] = box

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