from customtkinter import *
from classes.Id_generator import IdGenerator
from classes.Password_generator import PasswordGenerator
from classes.Dates_converter import Dates_converter
from classes.Lorem_generator import LoremGenerator
from classes.Emoji_converter import EmojiConverter
from classes.Unities_converter import UnitiesConverter

screen = CTk()
screen.minsize(width=900, height=500)
screen.maxsize(width=900, height=500)
screen.title('Utilities')
screen.iconbitmap('outils.ico')

set_appearance_mode('dark')
set_default_color_theme('green')

mode = 'ID-generator'


def change_mode(new_mode, button):
    global mode
    global result_input
    global id_generator
    global password_generator
    global dates_converter
    global lorem_generator
    global emoji_converter
    global markdown_previewer
    global unities_converter

    for btn in buttons:
        btn.configure(fg_color='#11B384', text_color='gray90')

    button.configure(fg_color='#085D45', text_color='#fff')

    mode = new_mode
    canvas.delete('all')

    if mode == 'ID-generator':
        id_generator = IdGenerator(canvas)

    elif mode == 'password-generator':
        password_generator = PasswordGenerator(canvas)

    elif mode == 'date-converter':
        dates_converter = Dates_converter(canvas)

    elif mode == 'lorem-generator':
        lorem_generator = LoremGenerator(canvas)

    elif mode == 'emoji-converter':
        emoji_converter = EmojiConverter(canvas)

    elif mode == 'unities-converter':
        unities_converter = UnitiesConverter(canvas)

    result_label = CTkLabel(text='Resulat', text_color='#fff')
    canvas.create_window(200, 270, window=result_label)

    result_input = CTkEntry(width=200, bg_color='gray12')
    canvas.create_window(200, 310, window=result_input)

    valid_button = CTkButton(text='Valider', command=valid)
    canvas.create_window(200, 370, window=valid_button)

    if mode == 'lorem-generator' or mode == 'markdown-previewer':
        result_input.destroy()
        result_label.destroy()

        result_label = CTkLabel(text='Resulat', text_color='#fff')
        canvas.create_window(200, 190, window=result_label)

        result_input = CTkTextbox(width=300, height=100, bg_color='gray12')
        canvas.create_window(200, 280, window=result_input)


def valid():
    global result_input

    if mode == 'ID-generator':
        result = id_generator.valid()

    elif mode == 'password-generator':
        result = password_generator.valid()

    elif mode == 'date-converter':
        result = dates_converter.valid()

    elif mode == 'lorem-generator':
        result = lorem_generator.valid()

    elif mode == 'emoji-converter':
        result = emoji_converter.valid()

    elif mode == 'unities-converter':
        result = unities_converter.valid()

    if mode == 'lorem-generator':
        result_input.destroy()

        result_input = CTkTextbox(width=300, height=100, bg_color='gray12')
        canvas.create_window(200, 280, window=result_input)

        result_input.insert('1.0', result)

    else:
        result_input.delete(0, END)
        result_input.insert(0, result)


menu = CTkCanvas(width=220, height=625, bg='#fff')
menu.place(x=0, y=0)

menu_button1 = CTkButton(text="Generateur d'ID", bg_color='#fff', fg_color='#085D45', text_color='#fff', command=lambda: change_mode('ID-generator', menu_button1))
menu.create_window(112, 30, window=menu_button1)

menu_button2 = CTkButton(text="Generateur de MDP", bg_color='#fff', command=lambda: change_mode('password-generator', menu_button2))
menu.create_window(112, 70, window=menu_button2)

menu_button3 = CTkButton(text="Convertisseur de dates", bg_color='#fff', command=lambda: change_mode('date-converter', menu_button3))
menu.create_window(112, 110, window=menu_button3)

menu_button4 = CTkButton(text="Generateur de lorem ipsum", bg_color='#fff', command=lambda: change_mode('lorem-generator', menu_button4))
menu.create_window(112, 150, window=menu_button4)

menu_button5 = CTkButton(text="Convertisseur de \n texte et caracteres speciaux", bg_color='#fff', command=lambda: change_mode('emoji-converter', menu_button5))
menu.create_window(112, 195, window=menu_button5)

menu_button6 = CTkButton(text="Converrtisseur d'unités", bg_color='#fff', command=lambda: change_mode('unities-converter', menu_button6))
menu.create_window(112, 240, window=menu_button6)

#---------------

canvas = CTkCanvas(width=400, height=400, bg='gray12')
canvas.place(x=450, y=50)

id_generator = IdGenerator(canvas)

result_label = CTkLabel(text='Resulat', text_color='#fff')
canvas.create_window(200, 270, window=result_label)

result_input = CTkEntry(width=200)
canvas.create_window(200, 310, window=result_input)

valid_button = CTkButton(text='Valider', command=valid)
canvas.create_window(200, 370, window=valid_button)

buttons = (menu_button1, menu_button2, menu_button3, menu_button4, menu_button5, menu_button6)

screen.mainloop()
