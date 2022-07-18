"""
Creating GUIs with tkinter
- Use canvas to draw
- handle mouse events

Version: 0.1
Author: author
Date: 2018-03-14
"""

import tkinter


def mouse_evt_handler(evt=None):
    row = round((evt.y - 20) / 40)
    col = round((evt.x - 20) / 40)
    pos_x = 40 * col
    pos_y = 40 * row
    canvas.create_oval(pos_x, pos_y, 40 + pos_x, 40 + pos_y, fill='black')


top = tkinter.Tk()
# set window size
top.geometry('620x620')
# set the window title
top.title('Gobang')
# Set the window size to be immutable
top.resizable(False, False)
# Set the window to the top
top.wm_attributes('-topmost', 1)
canvas = tkinter.Canvas(top, width=600, height=600, bd=0, highlightthickness=0)
canvas.bind('<Button-1>', mouse_evt_handler)
canvas.create_rectangle(0, 0, 600, 600, fill='yellow', outline='white')
for index in range(15):
    canvas.create_line(20, 20 + 40 * index, 580, 20 + 40 * index, fill='black')
    canvas.create_line(20 + 40 * index, 20, 20 + 40 * index, 580, fill='black')
canvas.create_rectangle(15, 15, 585, 585, outline='black', width=4)
canvas.pack()
tkinter.mainloop()

# Please think about how to encapsulate the above code with object-oriented programming ideas