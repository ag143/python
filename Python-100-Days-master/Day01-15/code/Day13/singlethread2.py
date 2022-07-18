"""
Without multithreading - time-consuming tasks block the main event loop

Version: 0.1
Author: author
Date: 2018-03-20
"""

import time
import tkinter
import tkinter.messagebox


def download():
    # The simulated download task takes 10 seconds
    time.sleep(10)
    tkinter.messagebox.showinfo('Prompt', 'Download complete!')


def show_about():
    tkinter.messagebox.showinfo('About', 'Author: author(v1.0)')


def main():
    top = tkinter.Tk()
    top.title('Single thread')
    top.geometry('200x150')
    top.wm_attributes('-topmost', True)

    panel = tkinter.Frame(top)
    button1 = tkinter.Button(panel, text='download', command=download)
    button1.pack(side='left')
    button2 = tkinter.Button(panel, text='about', command=show_about)
    button2.pack(side='right')
    panel.pack(side='bottom')

    tkinter.mainloop()


if __name__ == '__main__':
    main()


# without using multithreading once the download button is clicked because the operation takes 10 seconds
# The entire main message loop will also be blocked for 10 seconds and cannot respond to other events
# In fact, for subtasks that have no causal relationship, this sequential execution is not reasonable