#! /usr/bin/env python3
# -*- coding: utf-8 -*-

# Imports ######################################################################
import tkinter as tk
import classes as cls
import utils


# Global variables #############################################################
HEIGHT = 10
WIDTH = 15
BOMBS = 40
BOMBS_LEFT = BOMBS


# Main unresizable window ######################################################
window = tk.Tk()
window['bg'] = 'white'
window.resizable(width=False, height=False)


# Images #######################################################################
FLAG = tk.PhotoImage(file="red_flag.gif")
MINE = tk.PhotoImage(file="mine.gif")


# Game menu (will probably require a package) ##################################
menubar = tk.Menu(window)
menu1 = tk.Menu(menubar, tearoff=0)
menu2 = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="Fichier", menu=menu1)
menubar.add_cascade(label="Aide", menu=menu2)
window.config(menu=menubar)


# Top frame ####################################################################
top_frame = tk.Frame(window, borderwidth=2, height=40, relief=tk.GROOVE)
top_frame.pack(padx=0, pady=0, side=tk.TOP, fill="x")

# bombs_counter = tk.Label(top_frame, bg="#fff", text=game_grid.bombs_left)
# bombs_counter.pack(padx = 3, pady = 3, side=tk.LEFT, fill="x")


# Game frame ###################################################################
game_frame = tk.Frame(window, borderwidth=2, relief=tk.SUNKEN)

def create_square(i, j):
    s = cls.Square(i, j, game_frame, height=25, width=25)
    s.pack_propagate(False) # still useful ?
    s.grid_propagate(False) # still useful ?
    s.grid(row=i, column=j)
    return s

squares = [[create_square(i, j) for i in range(HEIGHT)] for j in range(WIDTH)]
utils.add_bombs(squares, BOMBS, HEIGHT, WIDTH)
game_frame.pack(padx=10, pady=10, side=tk.BOTTOM)



window.mainloop()
