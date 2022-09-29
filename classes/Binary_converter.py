from customtkinter import *
from helpers import create_error, alphabet_encode, alphabet_decode


class BinaryConverter():
    def __init__(self, canvas):
        self.canvas = canvas

        self.bin_var = StringVar()
        self.bin_var.set('texttobin')

        self.text_to_binary_switch = CTkRadioButton(text='Texte vers Binaire', value='texttobin',
                                                   variable=self.bin_var, bg_color='gray12', )
        self.canvas.create_window(200, 30, window=self.text_to_binary_switch)

        self.binary_to_text_switch = CTkRadioButton(text='Binaire vers Texte', value='bintotext',
                                                   variable=self.bin_var, bg_color='gray12')
        self.canvas.create_window(200, 70, window=self.binary_to_text_switch)

        self.text_label = CTkLabel(text='Votre texte', bg_color='gray12')
        self.canvas.create_window(200, 110, window=self.text_label)

        self.text_input = CTkEntry()
        self.canvas.create_window(200, 150, window=self.text_input)

    def valid(self):
        value = self.text_input.get()
        result = ''

        if self.bin_var.get() == 'texttobin':
            for val in value:
                for character in alphabet_encode:
                    if character == val:
                        result += f'{alphabet_encode[character]} '

        else:
            values = value.replace('\n', '').split(' ')
            values.append(' ')

            for val in values:
                for character in alphabet_decode:
                    if character == val:
                        result += alphabet_decode[character]

        return result
