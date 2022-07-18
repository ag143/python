"""
Creating GUIs with tkinter
- Top level window
- Controls
- Layout
- event callback

Version: 0.1
Author: author
Date: 2018-03-14
"""

import tkinter
import tkinter.messagebox


def main():
    flag = True

    # modify the text on the label
    def change_label_text():
        nonlocal flag
        flag = not flag
        color, msg = ('red', 'Hello, world!')\
            if flag else ('blue', 'Goodbye, world!')
        label.config(text=msg, fg=color)

    # confirm exit
    def confirm_to_quit():
        if tkinter.messagebox.askokcancel('Warm reminder', 'Are you sure you want to quit?'):
            top.quit()

    # create top-level window
    top = tkinter.Tk()
    # set window size
    top.geometry('240x160')
    # set the window title
    top.title('mini game')
    # create label object
    label = tkinter.Label(top, text='Hello, world!', font='Arial -32', fg='red')
    label.pack(expand=1)
    # Create a container for the button
    panel = tkinter.Frame(top)
    # create button object
    button1 = tkinter.Button(panel, text='modify', command=change_label_text)
    button1.pack(side='left')
    button2 = tkinter.Button(panel, text='quit', command=confirm_to_quit)
    button2.pack(side='right')
    panel.pack(side='bottom')
    # Start the main event loop
    tkinter.mainloop()


if __name__ == '__main__':
    main()