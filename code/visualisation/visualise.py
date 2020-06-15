from tkinter import Tk, Label, Button

import random 
import time

def visualise(init_game, result, board_size):
    root = Tk()
    root.title("Rush Hour")
    root.geometry('700x700')
    root.configure(bg='grey')

    veh_dict = {}
    counter = 0
    speed = 1

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

    def start():          
        stop = False
        for move in result['0']:
            while stop != True:
                time.sleep(speed)
                counter=+1
                car = veh_dict.get(move[0])
                for position in car.position:
                    boxes[position].configure(background='white')
                    
                for position in car.position:    
                    if car.orientation == 'horizontal':
                        print(car.position[1])
                        car.position[0][1] += move[1]
                        car.position[1][1] +=move[1]
                        boxes[position].configure(background=vehicle.color)
                    else:
                        car.position[0][0] +=move[1]
                        car.position[1][0] +=move[1]
                        boxes[position].configure(background=vehicle.color)
    def stop():
        stop = True

    startbtn = Button(root, text='Start', command=start).grid()
    startbtn = Button(root, text='Stop', command=stop).grid()
    root.mainloop()
            

       

        