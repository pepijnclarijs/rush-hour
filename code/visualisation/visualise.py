from tkinter import *

def visualise(board_size):
    window = Tk()
    window.title("Rush Hour")
    window.geometry('700x700')
    window.configure(bg='grey')
    
    for x in range(1, board_size+1):
        for y in range(1, board_size+1):
            box = Label(window, text=f'{x},{y}', bg='white', bd=40)
            # box.getattr(self, "lab"+str({x},{y}))
            box.grid(row=y, column=x, padx=5, pady=5)
    window.mainloop() 