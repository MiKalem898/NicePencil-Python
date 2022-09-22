from customtkinter import *
from helpers import create_error, unities, unities_codes
from pint import UnitRegistry

ureg = UnitRegistry()


class UnitiesConverter():
    def __init__(self, canvas):
        self.canvas = canvas
        self.choices = ('Distances', 'Durées', 'Masses', 'Vitesses', 'Bande Passante')
        self.unities = unities['distance']
        self.base_unity_var = StringVar()
        self.base_unity_var.set('km')
        self.searched_unity_var = StringVar()
        self.searched_unity_var.set('km')

        self.type_label = CTkLabel(text="Type d'unité")
        self.canvas.create_window(100, 30, window=self.type_label)
        self.type_option = CTkOptionMenu(values=self.choices, command=self.change_type)
        self.canvas.create_window(300, 30, window=self.type_option)

        self.value_label = CTkLabel(text="Valeur")
        self.canvas.create_window(200, 80, window=self.value_label)
        self.value_input = CTkEntry()
        self.canvas.create_window(100, 130, window=self.value_input)

        self.base_unity_option = CTkOptionMenu(values=self.unities, variable=self.base_unity_var)
        self.canvas.create_window(300, 130, window=self.base_unity_option)

        self.searched_unity_label = CTkLabel(text="Convertir en")
        self.canvas.create_window(200, 180, window=self.searched_unity_label)
        self.searched_unity_option = CTkOptionMenu(values=self.unities, variable=self.searched_unity_var)
        self.canvas.create_window(200, 230, window=self.searched_unity_option)

    def change_type(self, choice):
        if choice == 'Distances':
            self.unities = unities['distance']

        elif choice == 'Durées':
            self.unities = unities['time']

        elif choice == 'Masses':
            self.unities = unities['mass']

        elif choice == 'Vitesses':
            self.unities = unities['speed']

        elif choice == 'Bande Passante':
            self.unities = unities['passing-band']

        self.base_unity_var.set(self.unities[0])
        self.searched_unity_var.set(self.unities[0])

        self.base_unity_option.configure(values=self.unities, variable=self.base_unity_var)
        self.searched_unity_option.configure(values=self.unities, variable=self.searched_unity_var)

    def valid(self):
        type = self.type_option.get()
        value = self.value_input.get()
        searched_unity = self.searched_unity_option.get()
        new_unity = ''

        try:
            if type == 'Bande Passante':
                base_unity = float(value) * unities_codes[type][self.base_unity_option.get().split('/')[0]]
                searched_unity = searched_unity.split('/')[0]

                new_unity = str(base_unity.to(unities_codes[type][searched_unity])) + '/s'

            else:
                base_unity = float(value) * unities_codes[type][self.base_unity_option.get()]
                new_unity = base_unity.to(unities_codes[type][searched_unity])

        except:
            create_error()

        return new_unity
