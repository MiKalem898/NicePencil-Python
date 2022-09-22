from customtkinter import *
from helpers import create_error, text_to_emoji_codes, emoji_to_text_codes


class EmojiConverter():
    def __init__(self, canvas):
        self.canvas = canvas

        self.emoji_var = StringVar()
        self.emoji_var.set('texttoemoji')

        self.text_to_emoji_switch = CTkRadioButton(text='Texte vers Car. Speciaux', value='texttoemoji',
                                                       variable=self.emoji_var, bg_color='gray12',)
        self.canvas.create_window(200, 30, window=self.text_to_emoji_switch)

        self.emoji_to_text_switch = CTkRadioButton(text='Car. Speciaux vers Texte', value='emojitotext',
                                                       variable=self.emoji_var, bg_color='gray12')
        self.canvas.create_window(200, 70, window=self.emoji_to_text_switch)

        self.text_label = CTkLabel(text='Votre texte', bg_color='gray12')
        self.canvas.create_window(200, 110, window=self.text_label)

        self.text_input = CTkEntry()
        self.canvas.create_window(200, 150, window=self.text_input)

    def valid(self):
        value = self.text_input.get().lower()
        result = ''

        if self.emoji_var.get() == 'texttoemoji':
            for val in value:
                for character in text_to_emoji_codes:
                    if character == val:
                        result += f'{text_to_emoji_codes[character]}'

        else:
            for val in value:
                for character in emoji_to_text_codes:
                    if character == val:
                        result += emoji_to_text_codes[character]

        return result
