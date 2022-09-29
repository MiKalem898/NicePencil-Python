from customtkinter import *
from helpers import create_error


class ColorConverter():
    def __init__(self, canvas):
        self.canvas = canvas

        self.var = StringVar()
        self.var.set('hextorgb')

        self.value_var = StringVar()

        self.hex_to_rgb_button = CTkRadioButton(bg_color='gray12', text='hex => rgb', value='hextorgb', variable=self.var)
        self.canvas.create_window(200, 30, window=self.hex_to_rgb_button)

        self.rgb_to_hex_button = CTkRadioButton(bg_color='gray12', text='rgb => hex', value='rgbtohex', variable=self.var)
        self.canvas.create_window(200, 70, window=self.rgb_to_hex_button)

        self.value_label = CTkLabel(text=f'Votre couleur')
        self.canvas.create_window(200, 120, window=self.value_label)
        self.value_text = CTkEntry()
        self.canvas.create_window(200, 170, window=self.value_text)

    def valid(self):
        mode = self.var.get()
        value = self.value_text.get()

        if mode == 'hextorgb':
            value = value.lstrip('#')
            lv = len(value)

            try:
                result = tuple(int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))

            except:
                create_error()

            else:
                return result

        else:
            values = value.replace('(', '').replace(')', '').split(',')

            try:
                for val in values:
                    values[values.index(val)] = int(val)

                values = tuple(values)

                result = '#%02x%02x%02x' % values

            except:
                create_error()

            else:
                return result