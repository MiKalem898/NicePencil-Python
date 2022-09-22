from customtkinter import *
import random
from helpers import codes


class IdGenerator():
    def __init__(self, canvas):
        self.canvas = canvas
        self.maj_switch = CTkSwitch(text='Majuscules', bg_color='gray12')
        self.canvas.create_window(100, 30, window=self.maj_switch)

        self.hyphen_switch = CTkSwitch(text='Tirets', bg_color='gray12')
        self.canvas.create_window(300, 30, window=self.hyphen_switch)

    def valid(self):
        hyphens = self.hyphen_switch.get()
        maj = self.maj_switch.get()
        id = ''

        for i in range(16):
            id += random.choice(codes)

            if hyphens:
                if i == 3 or i == 7 or i == 11:
                    id += '-'

        if maj:
            result = id.upper()
            return result

        else:
            result = id
            return result