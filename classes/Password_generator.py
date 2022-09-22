from customtkinter import *
import random
from helpers import codes
from helpers import create_error, letters, numbers, symbols


class PasswordGenerator():
    def __init__(self, canvas):
        self.canvas = canvas

        self.letters_label = CTkLabel(text='Nombre de lettres')
        self.canvas.create_window(100, 30, window=self.letters_label)

        self.letters_input = CTkEntry()
        self.canvas.create_window(300, 30, window=self.letters_input)

        self.numbers_label = CTkLabel(text='Nombre de numeros')
        self.canvas.create_window(100, 70, window=self.numbers_label)

        self.numbers_input = CTkEntry()
        self.canvas.create_window(300, 70, window=self.numbers_input)

        self.symbols_label = CTkLabel(text='Nombre de symboles')
        self.canvas.create_window(100, 110, window=self.symbols_label)

        self.symbols_input = CTkEntry()
        self.canvas.create_window(300, 110, window=self.symbols_input)

        self.maj_switch_password = CTkSwitch(text='Majuscules', bg_color='gray12')
        self.canvas.create_window(200, 150, window=self.maj_switch_password)

    def valid(self):
        letters_number = self.letters_input.get()
        numbers_number = self.numbers_input.get()
        symbols_number = self.symbols_input.get()
        majs = self.maj_switch_password.get()

        if not letters_number.isdigit() or not numbers_number.isdigit() or not symbols_number.isdigit():
            error = create_error()

        else:
            the_letters = []
            password = []

            for _ in range(int(letters_number)):
                the_letters.append(random.choice(letters))

            for _ in range(int(numbers_number)):
                password.append(random.choice(numbers))

            for _ in range(int(symbols_number)):
                password.append(random.choice(symbols))

            if majs:
                for i in range(0, len(the_letters)):
                    if random.randint(0, 1) == 1:
                        the_letters[i] = the_letters[i].upper()

            password = password + the_letters
            random.shuffle(password)
            result = ''.join(password)
            return result
