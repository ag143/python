"""
When using multithreading - time-consuming tasks are executed in separate threads

Version: 0.1
Author: author
Date: 2018-03-20
"""

import time
import tkinter
import tkinter.messagebox
from threading import Thread


def main():

    class DownloadTaskHandler(Thread):

        def run(self):
            # The simulated download task takes 10 seconds
            time.sleep(10)
            tkinter.messagebox.showinfo('Prompt', 'Download complete!')
            # enable download button
            button1.config(state=tkinter.NORMAL)

    def download():
        # disable download button
        button1.config(state=tkinter.DISABLED)
        # Set the thread as a daemon thread through the daemon parameter (the main program will no longer retain execution when it exits)
        DownloadTaskHandler(daemon=True).start()

    def show_about():
        tkinter.messagebox.showinfo('About', 'Author: author(v1.0)')

    top = tkinter.Tk()
    top.title('Single thread')
    top.geometry('200x150')
    top.wm_attributes('-topmost', 1)

    panel = tkinter.Frame(top)
    button1 = tkinter.Button(panel, text='download', command=download)
    button1.pack(side='left')
    button2 = tkinter.Button(panel, text='about', command=show_about)
    button2.pack(side='right')
    panel.pack(side='bottom')

    tkinter.mainloop()


if __name__ == '__main__':
    main()