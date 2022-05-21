import random
import tkinter as tk

class Root(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("tictactoe(4me)")
        self.geometry('500x400')

        self.char_x = tk.PhotoImage(file='./char_x.png')
        self.char_o = tk.PhotoImage(file='./char_zero.png')
        self.empty = tk.PhotoImage()

        self.active = 'GAME ACTIVE'
        self.total_cells = 9
        self.line_size = 3
        self.computer = {'value': 1, 'bg': 'orange',
                         'win': 'COMPUTER WINS', 'image': self.char_x}
        self.user = {'value': self.line_size+1, 'bg': 'grey',
                     'win': 'USER WINS', 'image': self.char_o}
        self.board_bg = 'white'
        self.all_lines = ((0, 1, 2), (3, 4, 5), (6, 7, 8),
                          (0, 3, 6), (1, 4, 7), (2, 5, 8),
                          (0, 4, 8), (2, 4, 6))

        self.create_radio_frame()
        self.create_control_frame()
