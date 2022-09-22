from customtkinter import *
from helpers import create_error
from lorem_text import lorem


class LoremGenerator():
    def __init__(self, canvas):
        self.canvas = canvas

        self.choices = ('Paragraphes', 'Phrases', 'Mots')
        self.value_inside = StringVar()
        self.value_inside.set("Paragraphes")

        self.type_lorem_label = CTkLabel(text='Type de generation')
        self.canvas.create_window(200, 30, window=self.type_lorem_label)

        self.type_lorem_select = CTkOptionMenu(values=self.choices)
        self.canvas.create_window(200, 70, window=self.type_lorem_select)

        self.gen_number_lorem_label = CTkLabel(text='Nombre de generations')
        self.canvas.create_window(200, 110, window=self.gen_number_lorem_label)

        self.gen_number_lorem_input = CTkEntry()
        self.canvas.create_window(200, 150, window=self.gen_number_lorem_input)

    def valid(self):
        type = self.type_lorem_select.get()
        number = self.gen_number_lorem_input.get()
        result = ''

        if not number.isdigit():
            create_error()

        else:
            number = int(number)
            if type == 'Paragraphes':
                result = lorem.paragraphs(number)

            elif type == 'Phrases':
                for i in range(number):
                    result += lorem.sentence()

            if type == 'Mots':
                result = lorem.words(number)

            return result

