from tkinter import Tk, Label, Button

import random 
import time

from load import load_game

class Visualise:
    def __init__(self, init_game, result, board_size):

        self.init_game = init_game
        self.result = result
        self.board_size = board_size

        root = Tk()
        root.title("Rush Hour")
        root.geometry('700x700')
        root.configure(bg='grey')

        # startbtn = Button(root, text='Start', command=start)
        # startbtn.pack(expand=False)

        veh_dict = {}
        counter = 0
        speed = 0.2

        boxes = {}
        for row in range(1, board_size+1):
            for col in range(1, board_size+1):
                box = Label(root, text=f'{row},{col}', bg='white', bd=40)
                box.grid(row=row, column=col)
                boxes[(row, col)] = box

        for vehicle in init_game.vehicles:
            vehicle.color = ["#"+''.join([random.choice('0123456789ABCDEF') for j in range(6)])]
            veh_dict[vehicle.id] = vehicle
            for position in vehicle.get_position():
                boxes[position].configure(background=vehicle.color)      

        root.mainloop()  

        def start():          
            for move in result['0']:
                time.sleep(speed)
                counter=+1
                car = veh_dict.get(move[0])
                for position in car.position:
                    boxes[position].configure(background='white')
                    # if car.orientation = 'horizontal':
                    #     boxes[position].configure(background=vehicle.color)
                    print(position)

       

        