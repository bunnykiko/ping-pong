from tkinter import Tk
from solo import PingPongSolo
from ping_p0ong import GameMenu
from two import PingPong

def start_menu():
    root = Tk()
    menu = GameMenu(root)
    root.mainloop()

def start_game():
    root = Tk()
    game = PingPongSolo(root)
    root.mainloop()


def start_multigame():
    root = Tk()
    menu = PingPong(root)
    root.mainloop()