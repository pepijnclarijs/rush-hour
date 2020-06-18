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
        veh_dict[vehicle.id] = vehicle
        if vehicle.id != 'X':
            vehicle.color = ["#"+''.join([random.choice('0123456789ABCDEF') for j in range(6)])]
        else:
            vehicle.color = "red"    
        for position in vehicle.get_position():
            boxes[position].configure(background=vehicle.color)   

    def start():          
        stop = False
        for move in result['0']:
            time.sleep(speed)
            counter=+1
            car = veh_dict.get(move[0])
            print(car)
            # print(car.position[0][0])
            # print(car.position[1][0])
            print(move[1])
            new_col_2 = car.position[1][1] + int(move[1])
            for position in car.position:
                boxes[position].configure(background='white')
            car.set_position(car.speculate_new_position(-1))    
            for position in car.position:    
                if car.orientation == 'horizontal':
                    boxes[position].configure(background=vehicle.color)


    startbtn = Button(root, text='Start', command=start).grid() 
    # stopbtn = Button(root, text='Stop', command=stop_game).grid()
    root.mainloop()
            

       

        